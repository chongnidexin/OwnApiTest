import unittest
import json
from tools.http_request import HttpRequest
from tools.get_data import GetData
from tools.my_ddt import ddt, data  # 处理列表嵌套列表，列表嵌套字典
from tools.do_excel import DoExcel
from tools import project_path
from tools.my_log import MyLog
from tools.do_mysql import DoMysql
import time
from tools.get_user_info import GetUserInfo

# ts = int(time.time())
# key = "*z5!2p(jywsjf-==!x_m+r4!lbs-#(gab4+nqwyi#n$9-4&7h_"
from tools.read_config import ReadConfig

test_data = DoExcel.get_data(project_path.test_case_path)  # 执行所有用例
# sign = GetUserInfo().sign(key, ts, test_data[0]['data'][8:21])
my_logger = MyLog()
host = ReadConfig.get_config(project_path.case_config_path, 'MODE', 'host')


@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self, item):
        if json.dumps(item['data']).find('${pk}') != -1:
            query_sql = 'select id from wish where user_id=1119 order by update_time desc limit 1'
            pk = DoMysql().do_mysql(query_sql, 1)[0]
            item['data'] = json.dumps(item['data']).replace('${pk}', str(pk))
            setattr(GetData, 'pk', pk)
            item['data'] = json.loads(item['data'], strict=False)
        elif json.dumps(item['data']).find('${sign}') != -1:
            sign = GetData().api_sign()
            item['data'] = json.dumps(item['data']).replace('${sign}', str(sign))
            setattr(GetData, 'sign', sign)
            item['data'] = json.loads(item['data'], strict=False)
        elif json.dumps(item['data']).find('${ts}') != -1:
            ts = GetData().ts
            item['data'] = json.dumps(item['data']).replace('${ts}', str(ts))
            setattr(GetData, 'ts', ts)
            item['data'] = json.loads(item['data'], strict=False)
        elif json.dumps(item['data']).find('${user_id}') != -1:
            userId = GetData().user_id
            item['data'] = json.dumps(item['data']).replace('${user_id}', str(userId))
            setattr(GetData, 'user_id', userId)
            item['data'] = json.loads(item['data'], strict=False)
        elif json.dumps(item['data']).find('${msg_type}') != -1:
            msg_type = GetData().msg_type
            item['data'] = json.dumps(item['data']).replace('${msg_type}', str(msg_type))
            setattr(GetData, 'msg_type', msg_type)
            item['data'] = json.loads(item['data'], strict=False)
        elif json.dumps(item['data']).find('${publickey}') != -1:
            publickey = GetData().publickey
            item['data'] = json.dumps(item['data']).replace('${publickey}', str(publickey))
            setattr(GetData, 'publickey', publickey)
            item['data'] = json.loads(item['data'], strict=False)

        my_logger.debug("开始执行{0}接口".format(item['title']))
        my_logger.info(item['url'])
        my_logger.info("请求数据是：{}".format(data))
        res = HttpRequest.http_request(host+item['url'], item['data'], item['http_method'])
        my_logger.info("获取到的结果是：{}".format(res.json()))

        # for data in item['data']:
        #     my_logger.info("请求数据是：{}".format(data))
        #     res = HttpRequest.http_request(host+item['url'], data, item['http_method'])
        #     my_logger.info("获取到的结果是：{}".format(res.json()))

        # if res.cookies:  # 利用反射来存储cookie值
        #     setattr(GetCookie, 'Cooike', res.cookies)

        try:
            self.assertEqual(item['expected'], res.json()['returnCode'])
            TestResult = 'Pass'  # 成功的
        except AssertionError as e:
            TestResult = 'Failed'  # 失败的
            my_logger.error("{0}执行用例出错：{1}".format(item['title'], e))
            raise e
        finally:  # 不管是错还是对，里面的代码一定会执行
            #my_logger.info(res.json())
            DoExcel.write_back(project_path.test_case_path, item['sheet_name'], item['case_id'] + 1, str(res.json()),
                               TestResult)
        my_logger.debug("{}执行成功".format(item['title']))
        my_logger.info(res.json())

    def tearDown(self):
        pass


if __name__ == '__main__':
    pass
