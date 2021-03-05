import requests
from tools.my_log import MyLog

my_logger = MyLog()


class HttpRequest:
    @staticmethod
    def http_request(url, data, http_method, cookie=None):

        try:
            if http_method.upper() == 'GET':
                res = requests.get(url, data, cookies=cookie)
            elif http_method.upper() == 'POST':
                res = requests.post(url, data, cookies=cookie)
            elif http_method.upper() == 'DELETE':
                res = requests.delete(url, data=data)
            else:
                my_logger.info("输入的请求方法不正确")
        except Exception as e:
            my_logger.error("请求方法出错了{}".format(e))
        return res  # 返回结果


if __name__ == '__main__':
    inquire_url = "http://test.paquapp.com/api/v2/topic/reply/"
    inquire_data = {"id": "1425"}

    inquire_res = HttpRequest().http_request(inquire_url, inquire_data, 'delete')
    print(inquire_res.json())
