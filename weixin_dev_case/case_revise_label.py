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
        self.reviselabel_name = config.reviselabel_name

    def tearDown(self) -> None:
        self.session.close()

    def testcase_lable_05(self):
        self._testMethodName = 'case08'
        self._testMethodDoc = '验证修改标签是否成功'
        print('~~~~~~开始修改标签')
        response_select = get_api.select_label(self.session,self.HOSTS,self.APPID,self.SECRET)
        response_revise = get_api.revise_label(self.session,self.HOSTS,self.APPID,self.SECRET,self.reviselabel_name,response_select)
        body_revise = response_revise.json()
        # 修改成功：{'errcode': 0, 'errmsg': 'ok'}
        print('修改标签的响应信息是：%s' % body_revise)
        errorcode_revise = response_revise.json()['errcode']
        print('~~~~~~结束修改标签')
        self.assertEqual(errorcode_revise,0,'case08 验证修改标签成功')


    def testcase_lable_06(self):
        self._testMethodName = 'case09'
        self._testMethodDoc = '验证修改标签是否重复'
        print('~~~~~~开始修改标签2')
        response_select2 = get_api.select_label(self.session, self.HOSTS, self.APPID, self.SECRET)
        response_revise2 = get_api.revise_label(self.session, self.HOSTS, self.APPID, self.SECRET, self.reviselabel_name,
                                               response_select2)
        body_revise2 = response_revise2.json()
        print('修改标签的响应信息是：%s' % body_revise2)
        print('~~~~~~结束修改标签2')
        errorcode_revise2 = response_revise2.json()['errcode']
        print(errorcode_revise2)
        self.assertEqual(errorcode_revise2, 45157, 'case09 验证修改标签重复')

    def testcase_lable_07(self):
        self._testMethodName = 'case10'
        self._testMethodDoc = '验证修改标签名是否超过30位字符'
        print('~~~~~~开始修改标签3')
        response_select3 = get_api.select_label(self.session, self.HOSTS, self.APPID, self.SECRET)
        response_revise3 = get_api.revise_label(self.session, self.HOSTS, self.APPID, self.SECRET, self.reviselabel_name,
                                               response_select3)
        body_revise3 = response_revise3.json()
        print('修改标签的响应信息是：%s' % body_revise3)
        print('~~~~~~结束修改标签3')
        errorcode_revise3 = response_revise3.json()['errcode']
        print(errorcode_revise3)
        self.assertEqual(errorcode_revise3, 45158, 'case10 验证修改标签名超过30位字符')




if __name__ == '__main__':
    unittest.main(verbosity=2)
