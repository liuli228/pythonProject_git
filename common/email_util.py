import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.config_util import config

class EmailUtils:
    #smtp_body  邮件正文    smtp_attch_path 邮件附件获取文件的路径
    def __init__(self,smtp_body,smtp_attch_path=None):
        self.smtp_server = 'smtp.qq.com'
        self.smtp_port = 25
        self.smtp_sender = '294608794@qq.com'
        #密码要改成QQ开启服务的授权码
        self.smtp_password = 'jzqddxodcfccbjci'
        self.smtp_receiver = config.SMTP_RECEIVER
        self.smtp_cc = '329999897@qq.com,2431904050@qq.com'
        self.smtp_subject = 'liuli的微信接口自动化测试报告'
        self.smtp_body = smtp_body
        self.smtp_attch_path = smtp_attch_path

    def email_message_body(self):
        message = MIMEMultipart()
        message['from'] = self.smtp_sender
        message['to'] = self.smtp_receiver
        message['Cc'] = self.smtp_cc
        message['subject'] = self.smtp_subject
        message.attach( MIMEText(self.smtp_body,'html','utf-8') )
        if self.smtp_attch_path:
            attach_file_obj = MIMEText(open(self.smtp_attch_path, 'rb').read(), 'base64', 'utf-8')
            attach_file_obj['Content-Type'] = 'application/octet-stream'
            attach_file_obj.add_header('Content-Disposition', 'atachment',
                                       filename=('gbk', '', os.path.basename(self.smtp_attch_path)))
            message.attach(attach_file_obj)
        return message

    def send_mail(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server,self.smtp_port)
        smtp.login(self.smtp_sender,self.smtp_password)
        smtp.sendmail( self.smtp_sender,self.smtp_receiver.split(',')+self.smtp_cc.split(',')   ,self.email_message_body().as_string() )

if __name__=='__main__':
    email_u = EmailUtils('test使用','./API_TEST_V2.0.html')
    email_u.send_mail()
