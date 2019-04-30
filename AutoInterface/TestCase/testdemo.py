import json
import unittest

from BeautifulReport import BeautifulReport

from AutoInterface.Common import BaseHttp, Log, CommonData

Http =BaseHttp.SendHttp()
log = Log.log('Test Demo').get_logger()
# login = Base.Base()
class testdemo(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_addmicro(self):
        # login.login()
        f=CommonData.rwdata()
        dataq =f.get_alldata('Sheet1') #获取excel数据
        for valus in dataq:
            self.case_name=valus[0]
            self.method=valus[1]
            self.path = valus[2]
            self.headers=valus[3]
            # self.params=valus[7]
            self.data = valus[8]
            Http.set_url(self.path)
            if self.method =='GET'or self.method == 'get':
                Http.set_params(self.params)
                self.response =Http.http_cookie_get()
                log.info(self.response.text)
            elif self.method=='POST' or self.method=='post':
                # Http.set_params(self.params)
                strheader = json.loads(self.headers)
                Http.set_headers(strheader)
                strdata=json.loads(self.data)
                Http.set_data(strdata)
                self.response= Http.http_cookie_post()
                log.info(self.response.text)
        # print(type(self.response.status_code))
        # unittest.TestCase.assertEqual(self.response.status_code,200,'断言成功')
        # print("执行完成")
    def test_aa(self):
        print("ceshi")

if __name__ == '__main__':
    # suite=unittest.TestSuite()
    # suite.addTest(testdemo('test_aa'))
    # surun=unittest.TextTestRunner()
    # surun.run(suite)
    # print("py测试提交")
    suite_tests=unittest.defaultTestLoader.discover(".", pattern="*tests.py",
                                        top_level_dir=None)  # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    6
    BeautifulReport(suite_tests).report(filename='百度测试报告', description='搜索测试',
                                        log_path='.')  # log_path='.'把report放到当前目录下
    # unittest.main()