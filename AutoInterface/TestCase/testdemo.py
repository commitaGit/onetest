import json
import unittest

from BeautifulReport import BeautifulReport
from AutoInterface.Common import BaseHttp, Log, operationExcel

Http =BaseHttp.SendHttp()
class testdemo(unittest.TestCase):

    # def test_addmicro(self):
    #     # login.login()
    #     f=operationExcel.operationExcel()
    #     dataq =f.get_alldata('Sheet1') #获取excel数据
    #     for valus in dataq:
    #         self.case_name=valus[0]
    #         self.method=valus[1]
    #         self.path = valus[2]
    #         self.headers=valus[3]
    #         # self.params=valus[7]
    #         self.data = valus[8]
    #         Http.set_url(self.path)
    #         if self.method =='GET'or self.method == 'get':
    #             Http.set_params(self.params)
    #             self.response =Http.http_cookie_get()
    #             log.info(self.response.text)
    #         elif self.method=='POST' or self.method=='post':
    #             # Http.set_params(self.params)
    #             strheader = json.loads(self.headers)
    #             Http.set_headers(strheader)
    #             strdata=json.loads(self.data)
    #             Http.set_data(strdata)
    #             self.response= Http.http_cookie_post()
    #             log.info(self.response.text)
    #     # print(type(self.response.status_code))
    #     # unittest.TestCase.assertEqual(self.response.status_code,200,'断言成功')
    #     # print("执行完成")
    """ 测试代码生成与loader 测试数据"""

    def test_equal(self):
        import time
        time.sleep(1)
        self.assertTrue(1 == 1)

    def test_faile(self):
        assert  2==1

    @unittest.skip("暂不测试")
    def test_faile2(self):
        assert 2 == 1

if __name__ == '__main__':
    pass

