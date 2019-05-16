# import sys
# sys.path.append('E:/autoInterface/AutoInterface')
import os
import unittest
import time
from BeautifulReport import BeautifulReport
from AutoInterface.Common.Email import send_email
from AutoInterface.Common import Log

'''
自动化测试运行主方法
'''
class run:

    def __init__(self):
        self.logger = Log.log('run_main').logger

    def run_test(self):
       dirpath = os.path.abspath(os.path.dirname(os.getcwd()))
       report_path = os.path.join(dirpath, 'AutoInterface', 'Report')
       user_list = "hoze163@163.com,zhengwenpei@tehang.com"
       test_suite = unittest.defaultTestLoader.discover('./TestCase', pattern='test*.py')
       now_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
       result = BeautifulReport(test_suite)
       result.report(filename='自动化测试报告' + now_time, description='特航接口自动化测试报告', log_path=report_path)
       self.logger.info("================运行完成，请查看结果===============")
       context = '特航接口自动化测试Demo：' \
                 '  本次运行成功：XXX个' \
                 '           失败：XXX个''' \
                 '测试demo非真实==========='
       sen = send_email().send_mail(user_list, u'自动化测试报告', context)
       self.logger.info("邮件发送结果：",sen)





if __name__ == '__main__':
    run().run_test()
