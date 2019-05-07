import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('../TestCase', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='自动化测试报告', description='特航接口自动化测试报告', log_path='.')