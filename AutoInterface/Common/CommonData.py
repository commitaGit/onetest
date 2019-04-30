'''
读取跟设置数据（Excel和XML）
#TODO:当前实现默认为sheet第一个表 index=0
'''
import os

import xlrd
# from common import Log
from AutoInterface.Common import Log


class rwdata:
    def __init__(self):
        self.logger = Log.log('excel_log').logger
        # dirpath = os.path.split(__file__)[0]
        dirpath=os.path.pardir
        path = os.path.join(dirpath, 'TestFile','testdata.xlsx')
        if not os.path.exists(path):
            self.logger.error("没有用例Excel，请创建并确认有数据")
        else:
            #初始化实例并打开excel文档
            self.rwexcel = xlrd.open_workbook(path,encoding_override='utf-8')
            self.index=0



#获取表中某个shell所有的数据
    def get_alldata(self):
        try:
            data=[]
            shelldata=self.rwexcel.sheet_by_index(self.index)
            countrows = shelldata.nrows  #总行数
            countcols = shelldata.ncols     #总列数
            for i in range(countrows):
                rowdata=shelldata.row_values(i)
                if rowdata[0]!='case_name':
                    data.append(rowdata)
            return data
        except :
            raise xlrd.XLRDError('xlrd异常中断')
            self.logger.error("Excel文件错误")


#获取行的数据
    def get_rowdata(self,rowIndex):
        shelldata=self.rwexcel.sheet_by_index(self.index)
        str=shelldata.row_values(rowIndex)
        return str


#获取某一列的内容
    def get_coldata(self,colIndex):
        shelldata=self.rwexcel.sheet_by_index(self.index)
        str=shelldata.col_values(colIndex)
        return str





#获取单元格的行数

#获取某一个单元格的内容

#写入数据
    def write_value(self,row,col,value):
        shelldata=self.rwexcel.sheet_by_index(self.index)


#TODO:根据对应的caseid找到对应的行号
#TODO:根据行号，找到该行的内容
#TODO:根据对应的caseid找到对应行内容
#TODO:获取依赖数据的key
#TODO：判断是否有case依赖
#TODO:获取数据依赖字段


if __name__ == '__main__':
    rt = rwdata().get_alldata()
    print(rt)

