import pytest
import requests


class TestV2exApiWithParams(object):
    # domain = 'https://www.v2ex.com/'
    # @pytest.fixture(scope='function')
    # def setup_class(self):
    #
    #     print("setup_function():每个方法之前执行")
    #
    # @classmethod
    # def teardown_class(self):
    #     print("teardown_function():每个方法之后执行")

    @pytest.fixture

    def lang(request):
        # print('XXXXXXXXXXXXXXXXXXXXXXXXX',slef)
        print(__name__)
        return requests.post('https://test-staff-api-gateway-train.teyixing.com//v1/staff/login',data={"identity": "10001", "password": "d16caebd-eda8-4ab3-accb-2a0b1dc89c14", "clientType": "Admin"},headers={'Content-Type': 'application/json'},verify=False)
        # return request.param


    # def test_one(self):
    #     x = "this"
    #     # print('dasdasdsd')
    #     int2= 1 + 1
    #     assert int2==2
    # @staticmethod
    @pytest.mark.xfail(reason="判断失败")
    def test_two(self,lang):
        # print('======================',slef)
        print("pass")

        # print(lang.status_code)
        assert lang.status_code==200




if __name__=='__main__':
    TestV2exApiWithParams.test_two()
    # sa=TestV2exApiWithParams()
    # sa.test_two('ceshi')
    # assert si.status_code==200
    # print(si.status_code)

