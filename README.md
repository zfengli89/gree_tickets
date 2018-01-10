# gree_tickets
## author: 260216
###12306 grab tickets

#### 1/ 环境需求
#####    一 浏览器配置
    (1) 50以下的低版本firefox浏览器请更新到高版本,
        更新步骤参考博客(firefox无需下载了，本工程soft目录下含有最新版本浏览器软件)：http://blog.csdn.net/aoshilang2249/article/details/48630129
    (2) 安装geckodriver驱动，将soft目录下的geckodriver解压放入本机/usr/local/bin/；
#####    二 python配置
    (2) 安装aconoda2版本,python3的朋友应该也是可以的；
    (3) 安装splinter包: sudo pip install splinter；

#### 2/ 使用步骤
    (1) 需要一个12306的帐号，并在帐号中增加需要订票的乘车人信息；
    (2) conf/config.py为配置文件，里面包含乘车人的车次，日期，座位类型，站点（站点被12306转码，需要自己去cookies找到）等等，
        修改为自己想要的信息即可；
    (3) python 启动main.py；
    (4) 会弹出一个火狐模拟浏览器的登陆界面，输入帐号/密码/验证码，点击登陆，随后随意不要触碰浏览器了；
    (5) 程序会自动进行模拟点击并刷票，有余票时会自动提交订单，把它当作一个手速很快的男人即可；
    (6) 抢票完成，程序退出，请赶紧在30分钟内去付款结算；

#### 3/ bug
    程序不稳定，bug经常有，碰到异常退出可自行调试；
