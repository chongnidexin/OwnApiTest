import pymysql
from tools import project_path
from tools.read_config import ReadConfig


class DoMysql:

    def do_mysql(self, query_sql, state='all'):  # query --->查询语句
        # 利用这个类从配置文件中读取db info
        db_config = eval(ReadConfig().get_config(project_path.case_config_path, 'DB', 'db_config'))

        cnn = pymysql.connect(**db_config)

        # 游标cursor
        cursor = cnn.cursor()

        # 执行语句
        cursor.execute(query_sql)

        if state == 1:
            res = cursor.fetchone()  # 元组 针对一条数据
        else:
            res = cursor.fetchall()  # 列表 针对多条数据  列表嵌套元组

        # 关闭游标
        cursor.close()

        # 关闭连接
        cnn.close()
        return res


if __name__ == '__main__':
    query_sql = 'select max(id) from wish where user_id=1119'
    res = DoMysql().do_mysql(query_sql, 1)
    print(res)
