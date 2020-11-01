import unittest
import os
from common import HTMLTestReportCN
from common.email_util import EmailUtils

case_path = os.path.join( os.path.dirname(__file__),'weixin_dev_case' )
discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='case_*.py',
                                               top_level_dir=case_path)
all_case_suite = unittest.TestSuite()
all_case_suite.addTest( discover )

report_path = os.path.join(os.path.dirname(__file__),'report/')
report_dir = HTMLTestReportCN.ReportDirectory(report_path) #创建一个测试报告路径对象
report_dir.create_dir('API_TEST_') #调用创建目录的方法
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path') #获取测试报告文件的路径
report_html_file = open( report_html_path,'wb' )
html_runner = HTMLTestReportCN.HTMLTestRunner(stream=report_html_file,
                                              title='微信公众平台接口测试报告',
                                              description='接口框架测试实战使用',
                                              tester='work1015')
html_runner.run(all_case_suite)
EmailUtils('liuli发送的微信公共号接口测试报告，请查收。',report_html_path).send_mail()






