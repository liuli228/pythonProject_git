import requests
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
        self.createlabel_name = config.createlabel_name

    def tearDown(self) -> None:
        self.session.close()

    def testcase_lable_01(self):
        self._testMethodName = 'case04'
        self._testMethodDoc = '验证新建标签是否成功'
        print('~~~~~~开始新建标签')
        response_add = get_api.create_label(self.session, self.HOSTS, self.APPID, self.SECRET, self.createlabel_name)
        body_add = response_add.content.decode('utf-8')
        print('新建标签是：%s' % body_add)
        # 成功：{"tag":{"id":101,"name":"\\u65b0\\u5efa\\u6807\\u7b7e2"}}
        name_value = response_add.json()['tag']['name']
        print('~~~~~~结束新建标签')
        self.assertEqual(name_value, self.createlabel_name, 'case04 验证新建标签成功')

    def testcase_lable_02(self):
        self._testMethodName = 'case05'
        self._testMethodDoc = '验证新建标签是否重复'
        print('~~~~~~开始新建标签2')
        response_add1 = get_api.create_label(self.session, self.HOSTS, self.APPID, self.SECRET, self.createlabel_name)
        # {"errcode":45157,"errmsg":"invalid tag name hint: [mJhEmzNre-SKnlLA] rid: 5f883fc6-6259e32a-2ed1d305"}
        name_value = response_add1.json()['errcode']
        print('创建标签重复的返回码是：%s' % name_value)
        print('~~~~~~结束新建标签2')
        self.assertEqual(name_value, 45157, 'case05 验证新建标签重复')

    def testcase_lable_03(self):
        self._testMethodName = 'case06'
        self._testMethodDoc = '验证标签名长度是否超过30个字节'
        print('~~~~~~开始新建标签3')
        response_add3 = get_api.create_label(self.session, self.HOSTS, self.APPID, self.SECRET, self.createlabel_name)
        # {"errcode":45157,"errmsg":"invalid tag name hint: [mJhEmzNre-SKnlLA] rid: 5f883fc6-6259e32a-2ed1d305"}
        name_value3 = response_add3.json()['errcode']
        print('创建标签重复的返回码是：%s' % name_value3)
        print('~~~~~~结束新建标签3')
        self.assertEqual(name_value3, 45158, 'case06 验证标签名长度超过30个字节')



if __name__ == '__main__':
    unittest.main(verbosity=2)
