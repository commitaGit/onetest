import  jsonpath

from AutoInterface.Common.Base import Base
from AutoInterface.Common.BaseHttp import SendHttp
from AutoInterface.Utils import JsonUtil


class jsonpath_util:

    def get_values(self,json_obj,key):
        '''根据json获取key的values'''
        values =None
        if isinstance(json_obj,dict):
            values = jsonpath.jsonpath(json_obj,'$..%s' %(key))
            return  values
        else:
            values =jsonpath.jsonpath(json_obj.json(),'$..%s' %(key))
            return values






if __name__=="__main__":
    # parm = JsonUtil.OperetionJson().get_data('params')
    # h = SendHttp()
    # jstr = h.http_main('get', 'http://127.0.0.1:8181/matter/updateMatter', parm)
    # s=jsonpath_util().get_values(jstr,"msg")
    # print(s)
    re = Base()
    str = re.login()
    s1 = jsonpath_util().get_values(str, "name")
    print(s1)
