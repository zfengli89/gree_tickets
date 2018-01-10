#coding=utf-8
# author: 260216
from time import sleep
from splinter.browser import Browser
import conf.config as conf
from lxml import etree

class ticket():
    # 浏览器
    driver_name = None
    executable_path = None
    # 用户名，密码
    username = None
    passwd = None
    # 票信息
    starts = None
    ends = None
    dtime = None
    order = None
    userNames = None
    # 席位
    xb = None # 几等座
    pz = None # 票类型：成人 学生
    # 12306 urls
    ticket_url = None
    login_url = None
    initmy_url = None
    buy_url = None
    # driver
    driver = None

    def __init__(self,
                 driver_name,
                 executable_path,
                 username,
                 passwd,
                 starts,
                 ends,
                 dtime,
                 order,
                 userNames,
                 xb,
                 pz,
                 ticket_url,
                 login_url,
                 initmy_url,
                 buy_url):
        self.driver_name = driver_name
        self.executable_path = executable_path
        self.username = username
        self.passwd = passwd
        self.starts = starts
        self.ends = ends
        self.dtime = dtime
        self.order = order
        self.userNames = userNames
        self.xb = xb
        self.pz = pz
        self.ticket_url = ticket_url
        self.login_url = login_url
        self.initmy_url = initmy_url
        self.buy_url = buy_url
        self.setDriver()

    # set driver
    def setDriver(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        self.driver.driver.set_window_size(1400, 1000)

    # 需要人工输入验证码
    def login(self):
        conf.logger.info("登陆...")
        self.driver.visit(self.login_url)
        self.driver.fill("loginUserDTO.user_name", self.username)
        # sleep(1)
        self.driver.fill("userDTO.password", self.passwd)
        conf.logger.info("等待验证码，请人工自行输入...")
        while True:
            if self.driver.url != self.initmy_url:
                sleep(1)
            else:
                break

    # 选择乘客
    def choice_passengers(self):
        flag_suc = False
        for user in self.userNames:
            user_choice = self.driver.find_by_css("#normal_passenger_id").find_by_text(user)
            if 1 <= len(user_choice):
                user_choice.last.click()
                conf.logger.info("乘车人%s选择成功.", user.encode('utf-8'))
                flag_suc = True
            else:
                conf.logger.warn("乘车人%s不存在, 请确认乘车人信息是否正确.", user.encode('utf-8'))
        if not flag_suc:
            raise "乘车人信息有误,请检查."

    # 选择座位类型 返回 True：选择成功  Flase：选择失败
    def choice_seat(self):
        flag_choice = False
        # 点击选座按钮
        cnt_passagers = len(self.userNames)
        if cnt_passagers < 1:
            raise "未配置乘车人."
        for cnt in range(1, cnt_passagers+1):
            # 点击座位类型
            for seat_type in self.xb:
                seatId = "#seatType_" + str(cnt)
                self.driver.find_by_css(seatId).click()
                seat_butten = self.driver.find_by_value(seat_type)
                if seat_butten is None:
                    conf.logger.info("座位类型%s售空",seat_type)
                    continue
                if len(seat_butten) >= 1:
                    seat_butten.click()
                    flag_choice = True
                    conf.logger.info("选择座位成功！")
                    break
        return flag_choice

    # 增加cookies
    def add_cookies(self):
        # load cookies infomations
        self.driver.cookies.add({"_jc_save_fromStation": self.starts})
        self.driver.cookies.add({"_jc_save_toStation": self.ends})
        self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
        self.driver.reload()

    # 订票
    def book_ticket(self):
        cnt = 0
        while self.driver.url == self.ticket_url:
            # 查票
            conf.logger.info("查票")
            try:
                self.driver.find_by_text(u"查询").click()
                book_Elementlist = self.driver.find_by_text(u"预订")
                if len(book_Elementlist) > 0:
                    trains_indexs = []
                    selector = etree.HTML(self.driver.html)
                    act_trainsNums = list(selector.xpath('//tr/td/div/div/div/a/text()'))
                    for ord in self.order:
                        try:
                            index = act_trainsNums.index(ord)
                            trains_indexs.append(index)
                        except ValueError:
                            conf.logger.warn("找不到车次%s", ord)
                            pass
                    if len(trains_indexs) > 0:
                        for index in trains_indexs:
                            book_Elementlist[index].click()
            except Exception:
                conf.logger.warn("查询失败,网络不稳定.")
            finally:
                sleep(3)
                cnt = cnt + 1
                conf.logger.info("没有可预订的票, 第%d次查询余票.", cnt)

    def run(self):
        self.login()
        conf.logger.info("登陆成功")
        self.driver.visit(self.ticket_url)
        # set cookies
        conf.logger.info("输入查票信息")
        self.add_cookies()
        # 开始抢票
        while (1):
            # 预订
            self.book_ticket()
            # 选择乘车人
            self.choice_passengers()
            # 选座位等级
            if(self.choice_seat()):
                break
            else:
                conf.logger.info("需要的座位类型已售空,重新查询余票")
        sleep(1)
        # 订单提交
        self.driver.find_by_id('submitOrder_id').click()
        # 确认选座
        sleep(1)
        self.driver.find_by_id('qr_submit_id').click()
        # 抢票成功
        conf.logger.info("抢票成功,请在30分钟内去付款...")



