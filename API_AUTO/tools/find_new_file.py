import os
from tools import project_path
import datetime


def new_file_path():
    # 列出测试报告文件夹中的所有文件
    lists = os.listdir(project_path.test_report_path)

    # 按时间排序文件
    lists.sort(key=lambda fn: os.path.getctime(project_path.test_report_path + "/" + fn))

    # 获取到最新的文件保存到变量中
    new_file_path = os.path.join(project_path.test_report_path, lists[-1])

    return new_file_path


if __name__ == '__main__':
    print(os.path.split(new_file_path())[1])
