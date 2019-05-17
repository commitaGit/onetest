'''
读取跟设置数据（Excel和XML）
#TODO:当前实现默认为sheet第一个表 index=0
'''
import os

import xlrd
# from common import Log
from AutoInterface.Common import Log


class operationExcel:
    def __init__(self):
        self.logger = Log.log('operation_excel').logger
        # dirpath = os.path.split(__file__)[0]
        dirpath=os.path.pardir
        path = os.path.join(dirpath,'TestFile','interface_data.xlsx')
        try:
            self.rwexcel = xlrd.open_workbook(path, encoding_override='utf-8')
            self.index = 0
        except Exception as e:
            self.logger.error("没有用例Excel，请创建并确认有数据",e)

    #获取表中某个shell所有的数据
    def get_all_data(self):
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


#获取某一行的数据
    def get_row_data(self,rowIndex):
        shelldata=self.rwexcel.sheet_by_index(self.index)
        str=shelldata.row_values(rowIndex)
        return str


#获取某一列的内容
    def get_col_data(self,colIndex):
        shelldata=self.rwexcel.sheet_by_index(self.index)
        str=shelldata.col_values(colIndex)
        return str

#获取某一个单元格的内容
    def get_cell_value(self,row,col):
        shelldata = self.rwexcel.sheet_by_index(self.index)
        str = shelldata.cell_value(row,col)
        return str

# 获取单元格的行号
#     def get_cell_row(self,row):
#         shelldata = self.rwexcel.sheet_by_index(self.index)




#TODO:写入数据
    def write_value(self,row,col,value):
        shelldata=self.rwexcel.sheet_by_index(self.index)


#TODO:根据对应的caseid找到对应的行号
    def get_caseid_row(self):
        pass

#TODO:根据对应的caseid找到对应行内容
    def get_caseid_row_data(self):
        pass



#TODO:获取shell表总行数
    def get_shell_nrow(self):
        shelldata = self.rwexcel.sheet_by_index(self.index)
        countrows = shelldata.nrows
        return countrows


if __name__ == '__main__':
    rt = operationExcel().get_shell_nrow()
    print(rt)

