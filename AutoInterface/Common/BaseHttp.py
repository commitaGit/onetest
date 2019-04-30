import json
import os

import requests
from AutoInterface.Config import ReadConfig
from AutoInterface.Common import Log

'''封装HTTP请求实体类'''
'''当前服务器设定仅支持Tehang_5G内网访问'''
class SendHttp:
    def __init__(self):
        global httpscheme,baseurl,port,timeout
        loadRC = ReadConfig.readconfig()
        httpscheme = loadRC.get_URL('httpscheme')   #获取请求协议
        baseurl = loadRC.get_URL('baseurl')      #获取域名
        # port =loadRC.get_URL('port')
        self.timeout =loadRC.get_URL('timeout')
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url =None
        dirpath = os.path.split(__file__)[0]    #SSL证书配置
        self.path = os.path.join(dirpath, 'https.pem')
        self.logger = Log.log('https').logger


      #  self.files = {}
     #   self.state = 0


    def set_url(self,urlpath):
        self.url = (httpscheme+'://'+baseurl+urlpath).strip()
        self.logger.info('当前访问的地址为:'+self.url)


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
            # print('++++++++++++++++++++++++++++++++++',self.headers['Content-Type'])
            if  self.headers['Content-Type']=='application/json':
                rrdata=json.dumps(data)
                self.data = rrdata
            else:
                self.data =data

#'''get请求base配置,verify=False //关闭ssl校验'''
    def http_get(self):
        try:
            response = requests.get(self.url,params=self.params,headers=self.headers,timeout=float(self.timeout),verify=False)
            print(self.url)
            return  response
        except TimeoutError:
            #打印日志
            self.logger.error('GET请求失败')
            return None

#'''Post请求base配置'''
    def http_post(self):
        try:
            response = requests.post(self.url,data=self.data,headers=self.headers,timeout=float(self.timeout),verify=False)
            return  response
        #except TimeoutError:
        except Exception as e:
            #打印日志
            self.logger.error('Post请求失败',e)
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
    # basehttp =SendHttp()
    data = {"identity": "10001", "password": "d16caebd-eda8-4ab3-accb-2a0b1dc89c14", "clientType": "差大声大声道"}
    str=json.loads(data,ensure_ascii=False)
    # print(chardet.detect(json.dumps(data, ensure_ascii=False))) #编码识别模块
    print(str)
    # basehttp.set_url('/v1/staff/login')
    # basehttp.set_headers({'Content-Type':'application/json'})
    # basehttp.set_data(data)
    # response = basehttp.http_post()
    # print(response.json())