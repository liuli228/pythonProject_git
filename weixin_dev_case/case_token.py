import requests
import unittest
from common.config_util import config
from common import get_api
from nb_log import LogManager


class case_token(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
        self.APPID = config.appid
        self.SECRET = config.secret
        self.logger = LogManager('case_log').get_logger_and_add_handlers(10)

    def tearDown(self) -> None:
        self.session.close()

    def testcase_token_01(self):
        self._testMethodName = 'case01'
        self._testMethodDoc = '验证获取token是否成功'
        self.logger.info('获取tokencase01开始')
        reponse = get_api.get_response(self.session,self.HOSTS,self.APPID,self.SECRET)
        self.expirecode = reponse.json()['expires_in']
        print('获取token的返回码是：%s' % self.expirecode)
        self.assertEqual(self.expirecode,7200,'case01 验证获取token成功')
        self.logger.info('获取tokencase01结束：成功')

'''
    def testcase_token_02(self):
        self._testMethodName = 'case02'
        self._testMethodDoc = '验证grant_type字段值错误返回码是否正确'
        get_param_dict1 = {
            "grant_type": "client_credential1",
            "appid": self.APPID,
            "secret": self.SECRET
        }
        response1 = self.session.get(url='https://%s/cgi-bin/token' % self.HOSTS,
                                    params=get_param_dict1)
        self.expirecode1 = response1.json()['errcode']
        print('获取token的返回码是：%s' % self.expirecode1)
        self.assertEqual(self.expirecode1,40002,'case02 验证grant_type字段值错误返回码正确')


    def testcase_token_03(self):
        self._testMethodName = 'case03'
        self._testMethodDoc = '验证AppSecret错误返回码是否正确'
        get_param_dict2 = {
            "grant_type": "client_credential",
            "appid": self.APPID,
            "secret": 'd879ff27f0bacfb75cb65e56d35538fb1'
        }
        response2 = self.session.get(url='https://%s/cgi-bin/token' % self.HOSTS,
                                    params=get_param_dict2)
        self.expirecode2 = response2.json()['errcode']
        print('获取token的返回码是：%s' % self.expirecode2)
        self.assertEqual(self.expirecode2,40001,'case03 验证AppSecret错误返回码是否正确')
'''

if __name__=='__main__':
    unittest.main(verbosity=2)
