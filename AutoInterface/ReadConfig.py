import configparser
import os

'''读取配置文件'''

#读取当前Project下的配置文件config.ini
class readconfig:
    def __init__(self):
        path = os.path.split(__file__)[0]
        self.filepath = os.path.join(path,'config.ini')
        self.readconfig = configparser.ConfigParser()
        self.readconfig.read(self.filepath)
        # self.readconfig.write(filepath)

#获取HTTPURL配置信息
    def get_URL(self , name):

        self.name = self.readconfig.get('HTTPURL', name)
        return self.name

#获取HEADERS配置信息
    def get_Header(self, name):
        self.name = self.readconfig.get('HEADERS', name)
        return self.name

#获取HEADERS配置信息
    def get_DATABASE(self, name):
        self.name = self.readconfig.get('DATABASE', name)
        return self.name


    def set_Header(self,name,value):
        '''

        :param name: 需要设置的key
        :param value: 需要设置的value
        :return:
        '''

        self.readconfig.set('HEADERS',name,value)
        self.readconfig.write(open(self.filepath,'w'))
            #('C:/Users/hoze1/PycharmProjects/AutoInterface/config.ini','w')


if __name__ == '__main__':
    r=readconfig()
    # r.set_Header('MANAGER_TOKEN','QWK7uq5BvQKGIy55KFSbeAv77J1b4xN38lpzPEXf2eYaLq7RHVDH6p%2BLozOZ9O%2BROfDk0MV%2FBcxOkd1Iq1%2BBCALPp7EhXlRT6LM6avtf1EVIRkMq3%2F9tR9FMVqSuSMcQ')
    name=r.get_Header('MANAGER_TOKEN')
    # name=r.get_URL('port')

    print(name)