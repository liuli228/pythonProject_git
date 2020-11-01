import requests
import json
import jsonpath
import unittest
from common.config_util import config
from common import get_api


class case_lable(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
        self.APPID = config.appid
        self.SECRET = config.secret

    def tearDown(self) -> None:
        self.session.close()


    def testcase_lable_08(self):
        self._testMethodName = 'case11'
        self._testMethodDoc = '验证删除标签是否成功'
        print('~~~~~~开始删除标签')
        response_select = get_api.select_label(self.session, self.HOSTS, self.APPID, self.SECRET)
        response_delete = get_api.delete_label(self.session, self.HOSTS, self.APPID, self.SECRET,response_select)
        body_delete = response_delete.json()
        print('删除标签的响应信息是：%s'%body_delete)
        print('~~~~~~结束删除标签')
        errorcode_delete = response_delete.json()['errcode']
        self.assertEqual(errorcode_delete,0,'case11 验证删除标签标成功')




if __name__ == '__main__':
    unittest.main(verbosity=2)
