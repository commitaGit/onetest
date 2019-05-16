import os
import smtplib
import sys
from datetime import time
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from AutoInterface.Common import operationExcel

class send_email:
    '''
    发送邮件功能
    '''

    global send_user
    global email_host
    global password
    email_host = 'smtp.exmail.qq.com'
    send_user = "zhengwenpei@tehang.com"
    password = 'Zwp8999102'
    def __init__(self):
        self.data = operationExcel.operationExcel()
        # dirpath = os.path.pardir
        self.dirpath = os.path.abspath(os.path.dirname(os.getcwd()))
        self.report_path = os.path.join(self.dirpath,'AutoInterface', 'Report')

    def send_mail(self, user_list, sub, content):
        # msg = MIMEMultipart()
        # user = "接口自动化测试" + "<" + send_user + ">"
        user =send_user
        # message = MIMEText(content,_subtype='html',_charset='utf-8')
        message = MIMEMultipart()
        message['Subject'] = sub
        message['From'] = user  #发件人
        message['To'] = user_list #收件人
        # message['To'] = ";".join(user_list) #收件人

        message.attach(MIMEText(content, 'html', 'utf-8'))

        # 构造附件1，传送TestFile目录下的 interface_data.xlsx文件
        # dirpath=os.path.pardir
        path = os.path.join(self.dirpath, 'AutoInterface','TestFile', 'interface_data.xlsx')
        att1 = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 邮件中显示的附件名字
        att1["Content-Disposition"] = 'attachment; filename="interface_data.xlsx"'
        message.attach(att1)


        # 构造附件2，传送当前目录下的 report.html 文件
        #获取最新文件
        file_lists = os.listdir(self.report_path)
        file_lists.sort(key=lambda fn: os.path.getmtime(self.report_path + "\\" + fn)
        if not os.path.isdir(self.report_path + "\\" + fn) else 0)

        # dirpath = os.path.pardir
        # self.dirpath = os.path.abspath(os.path.dirname(os.getcwd()))
        path = os.path.join(self.dirpath, 'AutoInterface','Report', file_lists[-1])  #TODO：获取最新文件
        att2 = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2.add_header('Content-Disposition', 'attachment', filename=file_lists[-1])
        # att2["Content-Disposition"] = 'attachment;filename="自动化测试报告2019-05-14_16-00-08.html"'
        message.attach(att2)
        try:
            server = smtplib.SMTP()
            # server = smtplib.SMTP_SSL()
            server.set_debuglevel(1)
            server.connect(email_host,port=25)
            server.login(send_user, password)
            server.sendmail(user, user_list.split(','), message.as_string())
        except smtplib.SMTPException as e:
                print('无法发送邮件',e)
        finally:
            server.close()

    # def send_main(self, pass_list, fail_list):
    #     pass_num = float(len(pass_list))
    #     fail_num = float(len(fail_list))
    #     count_num = pass_num + fail_num
    #     # 90%
    #     pass_result = "%.2f%%" % (pass_num / count_num * 100)
    #     fail_result = "%.2f%%" % (fail_num / count_num * 100)
    #
    #
    #     user_list = ['zhengwenpei@tehang.com']
    #     sub = "接口自动化测试报告"
    #     # sub = "KevinAPIReport"
    #     # 将失败的接口在报告中展示
    #     caseId = []
    #     caseName = []
    #     header = []
    #     request_data = []
    #     url = []
    #     method = []
    #     is_run = []
    #     expect = []
    #     res = []
    #     result = []
    #     # 从excel中读取数据创建html
    #     for k in range(1, len(self.data.opera_excel.data)):
    #         caseIds = self.data.get_col(0, k)
    #         caseNmaes = self.data.get_col(1, k)
    #         headers = self.data.get_col(5, k)
    #         request_datas = self.data.get_col(9, k)
    #         urls = self.data.get_col(2, k)
    #         methods = self.data.get_col(4, k)
    #         is_runs = self.data.get_col(3, k)
    #         expects = self.data.get_col(10, k)
    #         ress = self.data.get_col(11, k)
    #         results = self.data.get_col(12, k)
    #         caseId.append(caseIds)
    #         caseName.append(caseNmaes)
    #         header.append(headers)
    #         request_data.append(request_datas)
    #         url.append(urls)
    #         method.append(methods)
    #         is_run.append(is_runs)
    #         expect.append(expects)
    #         res.append(ress)
    #         result.append(results)
    #     # failinfo = u""
    #     tab_info = ''
    #     for k in range(1, len(self.data.opera_excel.data)):
    #
    #         for i in range(1, len(res[k - 1])):
    #             if res[k - 1][i].encode('utf-8').startswith('fail'):
    #                 # failInfo1 = "接口用例id:%s 用例名称:%s，错误原因为 %s".decode('utf-8') %(int(caseId[i]),caseName[i],result[i])
    #                 # failinfo += failInfo1 + '\n'
    #                 # tab_info = createEmailInfo(caseId, caseName, request_data, url, result, res, is_run)
    #     if tab_info == '':
    #         content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s".decode('utf-8') % (
    #         count_num, pass_num, fail_num, pass_result,
    #         fail_result) + '<br><br>' + "详细报告：http://10.0.1.141:8000/index/".decode('utf-8') + "<br><br>"
    #     else:
    #         content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s".decode('utf-8') % (
    #         count_num, pass_num, fail_num, pass_result,
    #         fail_result) + '<br><br>' + "详细报告：http://10.0.1.141:8000/index/".decode('utf-8') + "<br><br>" \
    #                   + "<strong>" + "失败的用例如下：".decode('utf-8') + "</strong>" + "<br>" + tab_info.decode(
    #             'utf-8') + '<br><br>'
    #
    #     # content = "tota is %s，pass is %s，fail is %s,passed is %s,failed is %s" % (count_num, pass_num, fail_num, pass_result, fail_result)
    #     self.send_mail(user_list, sub, content)

    def find_new_file(self):

        '''查找目录下最新的文件'''
        file_lists = os.listdir(self.report_path )

        file_lists.sort(key=lambda fn: os.path.getmtime(self.report_path  + "\\" + fn)
        if not os.path.isdir(self.report_path  + "\\" + fn) else 0)
        # file = os.path.join(self.report_path , file_lists[-1])  #/全路径
        return file_lists[-1]

if __name__ == '__main__':

    # user_list="'zhengwenpei@tehang.com','hoze163@163.com'"
    user_list="hoze163@163.com,zhengwenpei@tehang.com"
    # user_list="hoze163@163.com"
    # ['john.doe@example.com', 'john.smith@example.co.uk']
    #554发送失败——解决方法：收件人加上发件人本身
    # file = send_email().find_new_file()
    # print(file)
    sen = send_email().send_mail(user_list,u'自动化测试报告','测试发送')
    print(sen)
