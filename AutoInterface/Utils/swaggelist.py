import requests
import jsonpath
import json
"""
遍历swagger接口文档

"""
#TODO： 接口获取后未保存，当前428个
class swagerlist:
    #获取swagger全部接口
    def get_swagger(self):
        i=0         #全量统计接口数量
        response = requests.get('https://dev-tmc-services.teyixing.com/v2/api-docs')
        result=jsonpath.jsonpath(response.json(),'$.paths')     #获取paths下所有接口路径，返回为list
        for z in result:
            # str =key
            str=z
            print(type(str))
        for key in str:
            print(key)
            i=i+1

        print(i)



if __name__== "__main__":
    swagerlist().get_swagger()