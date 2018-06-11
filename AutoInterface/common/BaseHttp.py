import json

import requests
import ReadConfig as RC
from  common import Log

'''封装HTTP请求实体类'''
class SendHttp:
    def __init__(self):
        global httpscheme,baseurl,port,timeout
        loadRC = RC.readconfig()
        httpscheme = loadRC.get_URL('httpscheme')   #获取请求协议
        baseurl = loadRC.get_URL('baseurl')      #获取域名
        port =loadRC.get_URL('port')
        self.timeout =loadRC.get_URL('timeout')
        #self.logger = Log.log().get_logger()
        # self.log = Log.get_log()
        # self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url =None
        self.cookie={'MANAGER_TOKEN':'zjiFwPnGq2RcZdrSA%2BEbj%2Fl8ElNblk%2BeNAoVfRJTQW7X12LDF%2BjNzS1bFiWlj4LUAyKpWUNJliRH9p6Trbhg1x05n7cLlbjghMJ%2BQmeDv%2Bb70Ej2lb0HjRCOa4cGU343'}


      #  self.files = {}
     #   self.state = 0


    def set_url(self,urlpath):
        self.url = httpscheme+'://'+baseurl+urlpath

    def set_headers(self,header):
        if not isinstance(header,dict):
            raise TypeError('header输入的类型不是dict类型')
        else:
            self.headers = header

    def set_params(self,params):
        if not isinstance(params,dict):
            raise TypeError('params输入的类型不是dict类型')
        else:
            self.params = params

    def set_data(self,data):
        if not isinstance(data,dict):
            raise TypeError('data输入的类型不是dict类型')
        else:
            if  self.headers['Content-Type']=='application/json':
                rrdata=json.dumps(data)
                self.data = rrdata
            else:
                self.data =data

#'''get请求base配置'''
    def http_get(self):
        try:
            response = requests.get(self.url,params=self.params,headers=self.headers,timeout=float(self.timeout))
            return  response
        except TimeoutError:
            #打印日志
            self.logger.error('GET请求超时')
            return None

#'''Post请求base配置'''
    def http_post(self):
        try:
            response = requests.post(self.url,data=self.data,headers=self.headers,timeout=float(self.timeout))
            return  response
        #except TimeoutError:
        except:
            #打印日志
            print('请求错误————————————————————————————')
            self.logger.error('Post请求超时')
            return None

#通过cookie请求
    def http_cookie_get(self):
        '''

        :param cookie:  登录态
        :return:
        '''
        session = requests.session()
        requests.utils.add_dict_to_cookiejar(session.cookies,self.cookie)
        response =session.get(self.url,params=self.params,headers=self.headers,timeout=float(self.timeout))
        return response

    def http_cookie_post(self):
        '''

        :param cookie: 登录态
        :return:
        '''
        session = requests.session()
        requests.utils.add_dict_to_cookiejar(session.cookies,self.cookie)
        response =session.post(self.url,data=self.data,headers=self.headers,timeout=float(self.timeout))
        return response

if __name__ == '__main__':
    jsondict=None
    re = SendHttp()
    re.set_url('/api/ng/microPage/list')
    data={'page':1,'pageSize':30,'xdpId':228,'order':1}
    re.set_params(data)
   # re.set_headers({'token':'aaaaa'})
   #  reap = re.http_get()
    reap=re.http_cookie_get()
    print(reap.text)
    # try:
    #     jsondict=json.loads(reap.json())
    # except TypeError :
    #     print("JSON类型错误")
    # print(jsondict)
    # if isinstance(rq,)rqisinstance