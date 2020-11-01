import requests
import json
import jsonpath
import unittest
from common.config_util import config
from common import get_api
from nb_log import LogManager


class case_lable(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
        self.APPID = config.appid
        self.SECRET = config.secret
        self.logger = LogManager('case_log').get_logger_and_add_handlers(10)

    def tearDown(self) -> None:
        self.session.close()

    def testcase_lable_04(self):
        self._testMethodName = 'case07'
        self._testMethodDoc = '验证查询标签是否成功'
        self.logger.info('查询标签开始')
        response_select = get_api.select_label(self.session,self.HOSTS,self.APPID,self.SECRET)
        body_select = response_select.content.decode('utf-8')
        self.logger.info('查询标签结果是：%s'%body_select)
        #str转dict
        json_data = json.loads(body_select)
        #list 列表+[0]=str
        select_name = jsonpath.jsonpath(json_data,'$.tags[0].name')[0]
        try:
            self.assertEqual(select_name,"星标组",'case07 验证查询标签成功')
            self.logger.info('查询标签结果：成功')
        except Exception as e:
            self.logger.debug('查询标签结果：失败，内容不匹配')

if __name__ == '__main__':
    unittest.main(verbosity=2)
