## 执行代码的入口
# from API_AUTO.tools.http_request import HttpRequest
# from API_AUTO.tools.do_excel import DoExcel
# from API_AUTO.tools.get_cookie import GetCookie

# test_data = [{"url": "http://op.juhe.cn/onebox/phone/query",
#               "data": {"tel": "15128288928", "dtype": "json", "key": "987ac050a14f34147396a2635657020f"},
#               "title": "电话号码归属地查询", "http_method": "post"}]
# cookie = None


# def run(test_data, sheet_name):
#     # global  cookie
#     for item in test_data:
#         print("执行执行的用例是:{0}".format(item["title"]))
#         res = HttpRequest().http_request(item["url"], eval(item["data"]), item["http_method"],getattr(GetCookie,'Cookie'))
#         if res.cookies:
#             # cookie=res.cookies
#             setattr(GetCookie,'Cookie',res.cookies)
#         print("请求的结果是:{0}".format(res.json()))
#         DoExcel().write_back('test_data/test_data.xlsx', sheet_name, item['case_id'] + 1, str(res.json()))
#
#         # inquire_url = "http://op.juhe.cn/onebox/phone/query"
#         # inquire_data = {"tel": "15128288928", "dtype": "json", "key": "987ac050a14f34147396a2635657020f"}
#         #
#         # inquire_res = HttpRequest().http_request(inquire_url, inquire_data, 'post')
#         # print(inquire_res.json())
#
#
# test_data = DoExcel().get_data('test_data/test_data.xlsx', 'inquire')
#
# run(test_data, 'inquire')

import unittest
import HTMLTestRunner

from tools.test_http_request import TestHttpRequest
from tools.project_path import *
from BeautifulReport import BeautifulReport
import time


now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
report_title = "paqu_api_" + now
desc = "玩具接口重构测试报告"

suite = unittest.TestSuite()
# suite.addTest(TestHttpRequest('test_api'))
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))


# with open(test_report_path, 'wb') as file:
#     # 执行用例
#     runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='这个是查询测试结果')
#     runner.run(suite)
runner = BeautifulReport(suite)
runner.report(description=desc, filename=report_title, report_dir=test_report_path)


if __name__ == '__main__':
    from tools.find_new_file import new_file_path
    from tools.send_email import SendEmail

    new_file_path = new_file_path()
    SendEmail().send_mail("guohongxin@popmart.com", new_file_path)

