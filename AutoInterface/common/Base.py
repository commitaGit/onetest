from common import BaseHttp
from common import Log
import ReadConfig


'''基本请求，登录登出'''
log=Log.log("Base login")
logger=log.get_logger
class Base:
    def __init__(self):
        self.basehttp = BaseHttp.SendHttp()
        self.readconfig=ReadConfig.readconfig()

    def login(self):
        data = {
            'password':'Seegohappy',
            'see_api_sign':'ac37953388831aaa0b756785a99c519e',
            'see_api_time':'20180604180696',
            'username':'superadmin@see'
        }

        self.basehttp.set_url('/api/auth/login')
        self.basehttp.set_params(data)
        response = self.basehttp.http_get()
        MANAGER_TOKEN=response.cookies.get('MANAGER_TOKEN')
        # print(MANAGER_TOKEN)
        # self.readconfig.set_Header('manager_token',MANAGER_TOKEN)

    def logout(self):
        self.basehttp.set_url('/api/auth/logout')
        response = self.basehttp.http_get()
        #print(response.text)


if __name__ == '__main__':
    re=Base()
    re.login()
