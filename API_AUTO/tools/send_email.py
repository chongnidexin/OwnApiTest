import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from tools.my_log import MyLog
from tools import project_path
from tools import find_new_file

# 邮件发送的用户名和密码   常识：第三方授权码
_user = "chongnidexin@yeah.net"
_pwd = "YSFRIAHRKWAOGTPO"
loger = MyLog()
now = time.strftime('%Y-%m-%d_%H_%M_%S')
new_file_path = find_new_file.new_file_path()
#print(new_file_path)


class SendEmail:

    def send_mail(self, email_to, filepath):
        # email_to 收件方
        # filepath 你要发送的附件地址
        # 如名字所示multipart就是分多个部分
        msg = MIMEMultipart()
        msg["Subject"] = now + '自动化测试报告'
        msg["From"] = _user
        msg["To"] = email_to

        # ---这是文字部分---
        part = MIMEText("这次是自动化测试结果，请查收")
        msg.attach(part)

        # ---这是附件部分---
        part = MIMEApplication(open(filepath, 'rb').read())
        part['Content-Type']='application/octet-stream'
        part.add_header('Content-Dispositon', 'attachment', filename=os.path.split(new_file_path)[1])

        msg.attach(part)
        s = smtplib.SMTP_SSL('smtp.yeah.net')  # 连接smtp邮件服务器，端口默认是25
        s.login(_user, _pwd)  # 登陆服务器
        s.sendmail(_user, email_to, msg.as_string())  # 发送邮件
        s.close()


if __name__ == '__main__':
    SendEmail().send_mail("guohongxin@popmart.com,361351168@qq.com", new_file_path)
