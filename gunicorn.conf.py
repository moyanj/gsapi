import multiprocessing
import sqlite3 as sql

# 连接到数据库
conn = sql.connect('db/config.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM config;')
rows = cursor.fetchall()
conf = {}
# 遍历数据
for row in rows:
    # 每行数据以元组形式返回。
    key = row[0]
    value = row[1]
    # 进行相应的操作，这里仅打印出数据
    conf[key] = value


bind = "{}:{}".format(conf["host"],conf["port"])

workers = multiprocessing.cpu_count() * 2 + 1

threads = 2

loglevel = "error"

worker_connections = 1000

preload_app = True
