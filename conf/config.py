# coding=utf-8
# author: 260216

# 模拟浏览器  高版本火狐需要geckodriver驱动
driver_name = "firefox"
executable_path = "/usr/local/bin/geckodriver"

# 12306
user = "*******@qq.com"
password = "******"

# 票信息
# 站点被转码，得自己去找对应的cookies值
from_station = u"%u5E7F%u5DDE%u5357%2CIZQ" #广州南
# from_station = u"%u73E0%u6D77%2CZHQ"     #珠海
to_station = u"%u5CB3%u9633%u4E1C%2CYIQ"   #岳阳东
departure_time = u"2018-01-16"
# 可接受的车次 顺序先后代表了优先级别
order = ["G1744345","G123"]
# 乘客
passengers = [u"丰", u"小陈陈"]

# 可以接受的座位等级,先后顺序代表优先级别
#  商务座:'9' 一等座: 'M' 二等座: 'O'
#  硬座：'1' 硬卧：‘3’ 软卧：4
xb = ["O", "M"]
# 成人票
pz = None

# WEB urls
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
buy_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"

#日志设置
import logging
logger = logging
logger.basicConfig(format= '%(asctime)s  %(filename)s : %(levelname)s  %(message)s',
                   datefmt= '%Y-%m-%d %A %H:%M:%S',
                   level= logging.INFO)