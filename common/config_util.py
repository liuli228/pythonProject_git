import os
import configparser

#:/0000Python学习/作业/work1015/common
#print(os.path.dirname(__file__))
#D:/0000Python学习/作业/work1015/common\..\connfig\config.ini
config_file_path = os.path.join( os.path.dirname(__file__) ,'..','connfig','config.ini' )

class ConfigUtils:
    def __init__(self,conf_path = config_file_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read( config_file_path ,encoding='utf-8')

    @property   # 类中的一个方法加property这个装饰器 属性方法
    def HOSTS(self):
        hosts_value = self.cfg.get('default','HOSTS')
        return hosts_value

    @property
    def appid(self):
        appid_value = self.cfg.get('default','appid')
        return appid_value

    @property
    def secret(self):
        secret_value = self.cfg.get('default','secret')
        return secret_value

    @property
    def createlabel_name(self):
        createlabel_name_value = self.cfg.get('default','createlabel_name')
        return createlabel_name_value

    @property
    def reviselabel_name(self):
        reviselabel_name_value = self.cfg.get('default','reviselabel_name')
        return reviselabel_name_value

    @property
    def REPORT_PATH(self):
        report_path_value = self.cfg.get('default','REPORT_PATH')
        return report_path_value

    @property
    def SMTP_RECEIVER(self):
        smtp_receiver_value = self.cfg.get('default', 'SMTP_RECEIVER')
        return smtp_receiver_value

config = ConfigUtils()

if __name__ == '__main__':
    print( config.HOSTS )

