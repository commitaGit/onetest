import logging
import os
'''AutoInterface 日志类'''


def golog(func):
    def funa(*args,**kw):
        print("装修函数")
        return func(*args,**kw)
    return funa


class log:
    #初始化日志
    def __init__(self,name):
        path = os.path.split(__file__)[0]
        filepath = os.path.join(path,'testlog.txt')
        self.logger=logging.getLogger(name) #'AutoInterface Log'
        self.logger.setLevel(logging.INFO)
        filehander = logging.FileHandler(filepath,encoding='UTF-8')
        systemhander = logging.StreamHandler()
        fileformatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
        filehander.setFormatter(fileformatter)
        self.logger.addHandler(systemhander)
        self.logger.addHandler(filehander)


    #获取实体
    @golog
    def get_logger(self):
        return self.logger





if __name__ == '__main__':
    f=log('999')
    f.get_logger().info(u'这是我的一个日志测试')
