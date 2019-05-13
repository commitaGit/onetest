# import sys
# sys.path.append('E:/autoInterface/AutoInterface')
import unittest
import time
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('../TestCase', pattern='test*.py')
    now_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    result = BeautifulReport(test_suite)
    result.report(filename='自动化测试报告'+now_time, description='特航接口自动化测试报告', log_path='.')
