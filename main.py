#coding=utf-8
# author: 260216
import src.ticket as tk
import conf.config as conf

if __name__ == '__main__':
    conf.logger.info('start grab ...')
    obj_ticket = tk.ticket(driver_name= conf.driver_name,
                 executable_path= conf.executable_path,
                 username= conf.user,
                 passwd= conf.password,
                 starts= conf.from_station,
                 ends= conf.to_station,
                 dtime= conf.departure_time,
                 order= conf.order,
                 userNames= conf.passengers,
                 xb= conf.xb,
                 pz= conf.pz,
                 ticket_url= conf.ticket_url,
                 login_url= conf.login_url,
                 initmy_url= conf.initmy_url,
                 buy_url= conf.buy_url)
    obj_ticket.run()
    conf.logger.info("program is stop.")

