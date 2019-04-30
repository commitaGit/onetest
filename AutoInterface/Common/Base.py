# import ReadConfig
from AutoInterface.Common import BaseHttp,Log
from AutoInterface.Config import ReadConfig

'''基本请求，登录登出'''

class Base:
    def __init__(self):
        self.logger=Log.log("Base_login").logger
        self.basehttp = BaseHttp.SendHttp()
        self.readconfig= ReadConfig.readconfig()

    def login(self):
        data = {"identity":"10001","password":"d16caebd-eda8-4ab3-accb-2a0b1dc89c14","clientType":"Admin"}

        self.basehttp.set_url('/v1/staff/login')
        self.basehttp.set_headers({'Content-Type':'application/json'})
        self.basehttp.set_data(data)
        response = self.basehttp.http_post()
        return response
        # MANAGER_TOKEN=response.cookies.get('MANAGER_TOKEN')
        # print(MANAGER_TOKEN)
        # self.readconfig.set_Header('manager_token',MANAGER_TOKEN)

#登出接口调用 //tehang没有logout
    def logout(self):
        self.basehttp.set_url('/api/auth/logout')
        response = self.basehttp.http_get()
        return response
        #print(response.text)


if __name__ == '__main__':
    re=Base()
    print(re.login().text)
