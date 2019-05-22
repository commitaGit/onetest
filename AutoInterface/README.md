# 接口自动化

> 使用到的模块
- requests
- xlrd
- jsonpath
- logging
- configparser

----------------------------
### 目录结构
> Common------公共方法 

>Config--------ini配置类

> Data------ 获取数据

>Log ------log归档存放

> Report ------报告归档存放

> TestCase ------测试用例

> TestFile ------测试数据驱动文件

> Utils ------工具类

> run.py ------主入口



### 使用方法

    例如：
    def test_getuser(self):
        '''测试登录后用户为后台管理员'''
        self.jutil = JsonPathUtil.jsonpath_util()
        self.basehttp.set_url('/v1/staff/login')
        self.basehttp.set_headers({'Content-Type':'application/json'})
        self.basehttp.set_data(data)
        response = self.basehttp.http_post()
        name = self.jutil.get_values(response,"name")
        for i in name:
            assert  i=="后台管理员"
