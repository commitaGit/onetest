import logging
import os
import time

'''AutoInterface 日志类'''


# def golog(func):
#     def funa(*args,**kw):
#         print("装修函数")
#         return func(*args,**kw)
#     return funa


class log:
    #初始化日志

    def __init__(self,name=None):
        now_time = time.strftime("%Y-%m-%d", time.localtime())
        path = os.path.abspath(os.path.dirname(os.getcwd())) #返回上级目录
        self.filepath = os.path.join(path,'Log','AutoInterfacelog_%s.log' %(now_time))
        self.logger=logging.getLogger(name) #'AutoInterface Log'
        self.logger.setLevel(logging.INFO)
        filehander = logging.FileHandler(self.filepath,encoding='UTF-8')
        systemhander = logging.StreamHandler()
        fileformatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
        filehander.setFormatter(fileformatter)
        systemhander.setFormatter(fileformatter)
        self.logger.addHandler(systemhander)
        self.logger.addHandler(filehander)


    #获取实体
    # @golog
    def get_logger(self):
        return self.logger





if __name__ == '__main__':
    f=log('LOG运行main方法')
    f.get_logger().info(u'这是我的一个日志测试')
    #E:\autoInterface\AutoInterface\Log\AutoInterfacelog_2019-05-16.log
#E:\\autoInterface\\Log\\AutoInterfacelog_2019-05-16.log'
    #E:\autoInterface\AutoInterface\Log\AutoInterfacelog_2019-05-16.log
