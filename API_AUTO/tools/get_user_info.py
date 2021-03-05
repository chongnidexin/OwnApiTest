import requests
import hashlib
import time
import xlrd
from tools import project_path


ts = int(time.time())
publickey = '''-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCI3ZvndV2627UcC/hRrKCr0yS5\nbrPgODNpj+ExNzKMEfHqc1LG+iFaOcuRy4Ukt/UdsVN/EoZU4BxaDoFHxZxcnA9t\nIYQ0F6QQxztgouRQ9r1W6szYvtX69iFLXiRqPRDSqKjO0WKzwacfMNCeqL/2zyaU\n4pmDBJZrmjb18xTCWwIDAQAB\n-----END PUBLIC KEY-----'''


class GetUserInfo():
    def login_sign(self):
        data = xlrd.open_workbook(project_path.test_case_path)
        table = data.sheet_by_name('init')
        key = "*z5!2p(jywsjf-==!x_m+r4!lbs-#(gab4+nqwyi#n$9-4&7h_"

        nrows = table.nrows
        for i in range(nrows):
            values = table.row_values(i, start_colx=0, end_colx=None)
            tel_num = str(int(values[0]))
            sign = hashlib.md5((key + tel_num + str(ts)).encode()).hexdigest()
        return sign

    def get_api_user_info(self):
        url = "http://test.paquapp.com/user/login/4/"
        req_body = {
            "tel": "15128283039",
            "code": "1234",
            "ts": ts,
            "sign": GetUserInfo().login_sign(),
            "client_public_key": publickey,
            "screen_width": 1080,
            "screen_height": 2016,
            "device_model": "16th",
            "device_identify": "60e71ae884988644",
            "system_version": "8.1.0",
            "version": "5.1.2",
            "platform": "Android",
            "net_status": 1
        }

        res = requests.post(url=url, data=req_body)
        api_user_info = {}
        api_user_info['token'] = res.json()['data']['token']
        api_user_info['user_id'] = res.json()['data']['address']['user_id']
        return api_user_info


if __name__ == '__main__':

    print(GetUserInfo().get_api_user_info())
