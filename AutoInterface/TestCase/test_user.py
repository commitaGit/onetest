import unittest
from AutoInterface.Common import Log, Base
from AutoInterface.Config import ReadConfig
from AutoInterface.Utils import JsonPathUtil
import sys
sys.path.append('E:/autoInterface/AutoInterface')
class log_user(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = Log.log("test_login").logger
        self.jutil = JsonPathUtil.jsonpath_util()

    def tearDown(self):
        pass


    def test_getuser(self):
        '''测试登录后用户为后台管理员'''
        re = Base.Base()
        response = re.login()
        name = self.jutil.get_values(response,"name")
        for i in name:
            assert  i=="后台管理员"

    # @unittest.expectedFailure
    # @unittest.skipIf(2>1,reason="a>b时，跳过处理")
    def test_get(self):
        '''后台管理员获取菜单权限'''
        assert 2==2





if __name__=='__main__':
    testsuite=unittest.TestSuite
    testsuite.addTest(log_user('test_getuser'))
    testsuite.addTest(log_user('test_get'))
    runner = unittest.TextTestRunner()
    runner.run(testsuite)
    log_user.test_log()


