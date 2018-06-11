'''读取跟设置数据（Excel和XML）'''
import xlrd
import os
from common import Log

class rwdata:
    def __init__(self):
        # path = 'C:/Users/hoze1/PycharmProjects/AutoInterface/testdata.xlsx'
        self.logger=Log.log('excel log').logger
        path = 'D:/testdata.xlsx'
        if not os.path.exists(path):
            # open(path,'a+')
            # self.rwexcel = xlrd.open_workbook(path)
            self.logger.error("没有用例Excel，请创建并确认有数据")
        else:
            self.rwexcel = xlrd.open_workbook(path,encoding_override='utf-8')



#获取表中某个shell所有的数据
    def get_alldata(self,shellname):
        try:
            data=[]
            shelldata=self.rwexcel.sheet_by_name(shellname)
            countrows = shelldata.nrows
            countcols = shelldata.ncols
            for i in range(countrows):
                rowdata=shelldata.row_values(i)
                if rowdata[0]!='case_name':
                    data.append(rowdata)
            return data
        except :
            raise xlrd.XLRDError('xlrd异常中断')
            self.logger.error("Excel文件错误")


#获取行的数据
    def get_rowdata(self,shellname,rowIndex):
        shelldata=self.rwexcel.sheet_by_name(shellname)
        str=shelldata.row_values(rowIndex)
        return str


#获取列的数据
    def get_coldata(self,shellname,colIndex):
        pass



if __name__ == '__main__':
    rt = rwdata().get_rowdata('Sheet1',1)
    print(rt)

