import logging
from tools import project_path
import time
import os


class MyLog:

    def __init__(self):
        self.log_name = os.path.join(project_path.log_path,
                                     '{0}.log'.format(time.strftime('%Y-%m-%d') + ' 接口日志'))

    def my_log(self, msg, level):

        my_logger = logging.getLogger('接口测试')
        my_logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于输出日志到文件
        fh = logging.FileHandler(self.log_name, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于输出日志到控制台
        kh = logging.StreamHandler()
        kh.setLevel(logging.DEBUG)

        # 定义handler输出格式
        formatter = logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-%(name)s--日志信息: %(message)s ')
        fh.setFormatter(formatter)
        kh.setFormatter(formatter)

        # 给logger添加 handler
        my_logger.addHandler(fh)
        my_logger.addHandler(kh)

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'Warning':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 关闭输出渠道
        my_logger.removeHandler(fh)
        my_logger.removeHandler(kh)
        fh.close()

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    pass
