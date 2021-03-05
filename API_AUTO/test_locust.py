
from locust import task, HttpLocust, TaskSet

from tools.read_config import ReadConfig
from tools.test_http_request import TestHttpRequest

from tools.do_excel import DoExcel
from tools import project_path
from tools.my_log import MyLog

test_data = DoExcel.get_data(project_path.test_case_path)
my_logger = MyLog()
host = ReadConfig.get_config(project_path.case_config_path, 'MODE', 'host')


# def encode(key, body, isgzip=True):
#     temp_key = key.encode('utf-8')
#     rc = ARC4.new(temp_key)
#     data = json.dumps(body)
#
#     if isgzip:
#         en_msg = rc.encrypt(gzip.compress(data.encode('utf-8')))
#     else:
#         en_msg = rc.encrypt(data.encode('utf-8'))
#     return en_msg


# 定义类（TaskSet任务集合）
class Work(TaskSet):

    # 定义方法
    @task(1)  # 定义任务权重（数值越大执行次数越多）
    def for_api_test(self):
        for item in test_data:
            # for data in item['data']:
            res = self.client.post(
                    item['url'], data=item['data'])
            print(res.status_code)


class Tadie(HttpLocust):
    task_set = Work
    min_wait, max_wait = 500, 1000
    host = host
    print(test_data)
