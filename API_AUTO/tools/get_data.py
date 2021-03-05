from pandas import options

from tools import project_path
import pandas as pd
import xlrd
from tools.get_user_info import GetUserInfo
from openpyxl import load_workbook
import time
import random
import rsa
import base64

import hashlib

secret_key = '''-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCI3ZvndV2627UcC/hRrKCr0yS5brPgODNpj+ExNzKMEfHqc1LG
+iFaOcuRy4Ukt/UdsVN/EoZU4BxaDoFHxZxcnA9tIYQ0F6QQxztgouRQ9r1W6szY
vtX69iFLXiRqPRDSqKjO0WKzwacfMNCeqL/2zyaU4pmDBJZrmjb18xTCWwIDAQAB
AoGAEDNXKHsqiJtIIVVDY/uQmzYngzGY5iIQ595plAdKGu1m2s8izb2+4+yybYQP
Mwz5XTXnwcNiFjre8EQGRoYcH2dSfg6vIBQQM1y36ZJrX9oaDSQvNKsMF4pLPAgX
v9SQTCO2cUsLxhenCMYaa1KKSxsbsfuQhU4ReK2+8eVZIiECQQCfkXC8pMx2eqdX
hRo9zYmtIa33cailySghSMv+W4sdphNAWdk/3Lgc2064HtHMt7xsmj81xCTeCs7M
3yCJiqPhAkEA25Pm8CDFEFBrsxbwmX7JWdB8RuKTmhsTqhF2PSAC7yqSZQnn6B0v
lrNpvKb+vabKL+Y1Qp8vgG3axQGmDBCtuwJBAIl5laaBWUKuU6RcoYojnf0Sqj4o
p0MGNtPOUyo2lnmZzrY/cqPJtrnt3DlXHCwDFIyAq/rXnWfL6fWqOu8lCiECQDdt
/r5fh1+27XkoMVSOTQX/O2Apklk0vKISBmcnzZXSiWI4PfK6a2j/oZGeFnCJykCN
PKS0yqkBEljpMaGaFEECQEnhqBL0+RsyXbd/xI7sJzmjbWFmjOexhluFa3+wUFWs
S/oSBrN3JjKRbjseM4YPzveCxgcWlF1KbFvk3OuHsPc=
-----END RSA PRIVATE KEY-----
'''


class GetData:
    # data = xlrd.open_workbook(project_path.test_case_path)
    # table = data.sheet_by_name('init')
    #
    # nrows = table.nrows
    # for i in range(nrows):
    #     values = table.row_values(i, start_colx=0, end_colx=None)
    #     tel_num = str(int(values[0]))
    #     wish_id = None
    #     sign = hashlib.md5((key + tel_num + str(ts)).encode()).hexdigest()
    # print((key + tel_num + str(ts)))

    Cookie = None
    wish_id = None
    ts = int(time.time())
    publickey = '''-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCI3ZvndV2627UcC/hRrKCr0yS5\nbrPgODNpj+ExNzKMEfHqc1LG+iFaOcuRy4Ukt/UdsVN/EoZU4BxaDoFHxZxcnA9t\nIYQ0F6QQxztgouRQ9r1W6szYvtX69iFLXiRqPRDSqKjO0WKzwacfMNCeqL/2zyaU\n4pmDBJZrmjb18xTCWwIDAQAB\n-----END PUBLIC KEY-----'''

    type = [1, 2, 3, 4, 5]
    msg_type = random.choice(type)
    user_info = GetUserInfo().get_api_user_info()
    token = user_info['token']
    user_id = user_info['user_id']

    # publickey = '''-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCI3ZvndV2627UcC/hRrKCr0yS5\nbrPgODNpj+ExNzKMEfHqc1LG+iFaOcuRy4Ukt/UdsVN/EoZU4BxaDoFHxZxcnA9t\nIYQ0F6QQxztgouRQ9r1W6szYvtX69iFLXiRqPRDSqKjO0WKzwacfMNCeqL/2zyaU\n4pmDBJZrmjb18xTCWwIDAQAB\n-----END PUBLIC KEY-----'''

    def decryptValue(self, value='', password=False):
        private_key = rsa.PrivateKey.load_pkcs1(secret_key)
        #print(value)
        value = base64.b64decode(value)
        value = rsa.decrypt(value, private_key)
        value = value[7:]
        if password:
            m = hashlib.md5()
            m.update(value)
            value = m.hexdigest()
        return value

    def api_sign(self):
        # print(self.decryptValue(token))


        api_sign = hashlib.md5(
            ("paquapp.com" + str(self.user_id) + self.decryptValue(self.token).decode() + str(self.ts)).encode()).hexdigest()
        # print(self.decryptValue(token).decode())
        # print("paquapp.com" + str(user_id) + self.decryptValue(token).decode() + str(self.ts))

        return api_sign
    # print(getattr(GetCookie, 'Cookie'))  # 获取属性值
    # setattr(GetCookie, 'Cookie', '123')  # set attribute 设置属性值
    # print(hasattr(GetCookie, 'Cookie'))  # 判断是否有这个属性
    # delattr(GetCookie, 'Cookie')  # 删除属性值
    #
    # print(hasattr(GetCookie,'Cookie'))
    #


if __name__ == '__main__':
    # pass
    print(GetData().api_sign())
