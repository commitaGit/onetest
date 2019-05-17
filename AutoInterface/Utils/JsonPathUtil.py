import  jsonpath

from AutoInterface.Common.Base import Base



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



#TODO:1\数据维护方式：1、excel  2、json  3、yaml   4、数据库



if __name__=="__main__":
    re = Base()
    str = re.login()
    s1 = jsonpath_util().get_values(str, "name")
    print(s1)
