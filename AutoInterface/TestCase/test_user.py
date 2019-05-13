import unittest
from AutoInterface.Common import Log, Base
from AutoInterface.Config import ReadConfig
import sys
sys.path.append('E:/autoInterface/AutoInterface')
class log_user(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = Log.log("test_login").logger

    def tearDown(self):
        pass


    def test_log(self):
        '''测试登录'''
        re = Base.Base()
        response = re.login()
        # loadRC = ReadConfig.readconfig()
        assert  response.status_code==200


if __name__=='__main__':
    log_user.test_log()


