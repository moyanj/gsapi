import os
import time
import datetime
import re #正则表达式
import requests as r #请求API
import json #数据解析

class Cache:

  def __init__(self, cache_dir='cache'):
    self.cache_dir = cache_dir

  def get(self, key):
    path = self._get_path(key)

    if os.path.exists(path):
      with open(path, 'r') as f:
        data = json.load(f)
        if self._is_expired(data):
          return None
        else:
          return data['value']
    else:
      return None

  def set(self, key, value, ttl=None):
    path = self._get_path(key)
    data = {'value': value, 'created_at': time.time(), 'ttl': ttl}
    with open(path, 'w') as f:
      json.dump(data, f)

  def get_all(self):
    all_data = {}
    for filename in os.listdir(self.cache_dir):
      path = os.path.join(self.cache_dir, filename)
      if os.path.isfile(path) and filename.endswith('.json'):
        with open(path, 'r') as f:
          data = json.load(f)
          if not self._is_expired(data):
            all_data[filename[:-5]] = data['value']
    return all_data

  def delete(self, key):
    path = self._get_path(key)
    if os.path.exists(path):
      os.remove(path)

  def delete_all(self):
    for filename in os.listdir(self.cache_dir):
      path = os.path.join(self.cache_dir, filename)
      if os.path.isfile(path) and filename.endswith('.json'):
        os.remove(path)

  def _get_path(self, key):
    filename = '{}.json'.format(key)
    path = os.path.join(self.cache_dir, filename)
    return path

  def _is_expired(self, data):
    if data['ttl'] and time.time() - data['created_at'] > data['ttl']:
      return True
    elif not data['ttl'] and time.time() - data['created_at'] > 60:
      return True
    else:
      return False
      
class Logger:
    def __init__(self, log_dir=None, level='INFO'):
        self.log_dir = log_dir if log_dir is not None else ''
        self.level = level

    def _write(self, msg):
        current_time = datetime.datetime.now()
        file_name = os.path.join(self.log_dir, f'{current_time.strftime("%Y-%m-%d")}.log')
        log_msg = f'[{current_time.strftime("%Y-%m-%d %H:%M:%S.%f")}] {msg}\n'
        with open(file_name, 'a') as f:
            f.write(log_msg)
        print(log_msg.strip())

    def debug(self, msg):
        if self.level in ['DEBUG', 'INFO']: 
            self._write(f'DEBUG - {msg}')

    def info(self, msg):
        if self.level in ['DEBUG', 'INFO', 'WARNING']:
            self._write(f'INFO - {msg}')

    def warning(self, msg):
        if self.level in ['DEBUG', 'INFO', 'WARNING', 'ERROR']:
            self._write(f'WARNING - {msg}')

    def error(self, msg):
        if self.level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            self._write(f'ERROR - {msg}')

    def critical(self, msg):
        if self.level == 'CRITICAL':
            self._write(f'CRITICAL - {msg}')

def req_enka(uid):
  from var import log,cache
  #设置ENKA API的URL
  url = "https://enka.network/api/uid/{}/".format(uid)
  #获取所有缓存
  cache_data = cache.get_all()
  #判断UID是否被缓存
  if "ysenka_"+uid in cache_data:
    #打印日志
    log.info("Cache yes")
    #返回数据，返回头，状态码
    return {"data": cache.get("ysenka_"+ uid), "headers": {"cache": "yes"}, "status": 200}
  else:
    #打印日志
    log.info("Cache no")
    #删除以前的缓存
    cache.delete(uid)
    #请求ENKA服务器
    enka_return = r.get(url)
    log.debug("Enka Status Code:{}".format(enka_return.status_code))
    if enka_return.status_code in [400,404,500,424,429,503]:
      log.error("ENKA Server Error")
      return {"data": "ENKA Server Error", "headers": {"cache": "no"}, "status": 202}
    else:
      #解析json
      enka_data = json.loads(enka_return.text)
    
      #设置缓存
      cache.set("ysenka_"+ uid, enka_data, ttl=300)
      #返回数据，返回头，状态码
      return {"data": enka_data, "headers": {"cache": "no"}, "status": 200}

#验证uid
def verifyUid(uid):
  from var import log
  #调用search函数
  regular = re.match("^[^34]\d{8}$",uid)
  #判断返回结果
  if regular == None:
    log.warning("Incorrect UID for user request query")
    return "no"
  else:
    return "yes"
#每个视图函数都有的方法
def viewFun(request):
  #输出log
  
  uid = request.values.get("uid")
  #验证UID是否有效
  if verifyUid(uid) == "no":
    return {"data":"Is not the correct UID","headers":{},"status":201}
  else:
    return req_enka(uid)
    
def req_eli(uid):
  from var import log,cache
  #设置ENKA API的URL
  url = "https://avocado.wiki/v1/info/{}/".format(uid)
  #获取所有缓存
  cache_data = cache.get_all()
  #判断UID是否被缓存
  if "sreli_"+uid in cache_data:
    #打印日志
    log.info("Cache yes")
    #返回数据，返回头，状态码
    return {"data": cache.get("sreli_"+uid), "headers": {"cache": "yes"}, "status": 200}
  else:
    #打印日志
    log.info("Cache no")
    #删除以前的缓存
    cache.delete(uid)
    #请求鳄梨API服务器
    try:
        eli_return = r.get(url)
    except:
      log.error("ELi Server Error")
      return {"data": "ELi Server Error", "headers": {"cache": "no"}, "status": 202}
    else:
      log.debug("ELi Status Code:{}".format(eli_return.status_code))  
      #解析json
      eli_data = json.loads(eli_return.text)
    
      #设置缓存
      cache.set("sreli_"+uid, eli_data, ttl=300)
      #返回数据，返回头，状态码
      return {"data": eli_data, "headers": {"cache": "no"}, "status": 200}
