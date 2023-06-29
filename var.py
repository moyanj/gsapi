import fun as lib
import time
import json
import hashlib as hl

f = open("config.json")
conf = json.load(f)
conf_ck = conf["cookie"]
conf_log = conf["log"]
conf_cache = conf["cache"]
conf_chat = conf["chat"]

log = lib.Logger(level=conf_log["level"], log_dir=conf_log["dir"])
#log.info("开始初始化缓存")
cache = lib.Cache(cache_dir=conf_cache["dir"])
#log.info("缓存初始化完毕")

def req_id(req_num):
  tmp = str(req_num+2*56)
  tmp2 = tmp + str(time.time())
  tmp3 = tmp2 + conf_ck["key"]
  log.debug("request ID plaintext："+tmp3)
  sha1 = hl.sha1()
  sha1.update(tmp3.encode("utf-8"))
  return sha1.hexdigest() 
  
#设置BosClient的Host，Access Key ID和Secret Access Key
f = open("data/img_source.json")
img_source = json.load(f)["data"]