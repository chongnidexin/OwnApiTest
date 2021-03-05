import os

"""专门用来读取路径的值"""
# 获取顶级文件路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 获取测试用例路径
test_case_path = os.path.join(project_path, 'test_data', 'test_data.xlsx')

# 获取测试报告路径
test_report_path = os.path.join(project_path, 'test_result', 'html_report')

# 配置文件路径
case_config_path = os.path.join(project_path, 'conf', 'case.config')

# 日志文件路径
log_path = os.path.join(project_path, 'test_result','log')
if __name__ == '__main__':
    print(project_path)
    print(test_report_path)
    print(log_path)
    print(case_config_path)
