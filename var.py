import fun as lib
import time
import json
import hashlib as hl
import sqlite3 as sql

conf = {}
#连接至数据库
conn = sql.connect('db/config.db')
cursor = conn.cursor()
# 获取所以value

cursor.execute('SELECT * FROM config;')
rows = cursor.fetchall()

# 遍历数据
for row in rows:
    # 每行数据以元组形式返回。
    key = row[0]
    value = row[1]
    # 进行相应的操作，这里仅打印出数据
    conf[key] = value

# print(conf)

log = lib.Logger(level=conf["log.level"], log_dir=conf["log.path"])
#log.info("开始初始化缓存")
cache = lib.Cache(cache_dir=conf["cache.path"])
#log.info("缓存初始化完毕")

def req_id(req_num):
  tmp = str(req_num+2*56)
  tmp2 = tmp + str(time.time())
  tmp3 = tmp2 + conf["cookie.key"]
  log.debug("request ID plaintext："+tmp3)
  sha1 = hl.sha1()
  sha1.update(tmp3.encode("utf-8"))
  return sha1.hexdigest() 
  
#设置BosClient的Host，Access Key ID和Secret Access Key
f = open("data/img_source.json")
img_source = json.load(f)["data"]