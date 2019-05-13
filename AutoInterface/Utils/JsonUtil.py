import json
import os


class OperetionJson:
    def __init__(self, file_path=None):
        if file_path == None:
            path=os.path.split(__file__)[0]
            self.file_path = os.path.join(path,"tjson.json")
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, id):
        return self.data[id]
        # try:
        #     jdata=self.data[id]
        # except KeyError as e:
        #     print('JSON找到该id：',e)
        # return jdata

    # 写json
    def write_data(self, data):
        with open(self.file_path, 'w') as fp:
            fp.write(json.dumps(data))

if __name__ == '__main__':
    opjson = OperetionJson()
    print(opjson.get_data('data'))