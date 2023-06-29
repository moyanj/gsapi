import re #正则表达式
from var import log,cache
import requests as r #请求API
import json #数据解析

def req_enka(uid):
  #设置ENKA API的URL
  url = "https://enka.network/api/uid/{}/".format(uid)
  #获取所有缓存
  cache_data = cache.get_all()
  #判断UID是否被缓存
  if uid in cache_data:
    #打印日志
    log.info("Cache yes")
    #返回数据，返回头，状态码
    return {"data": cache.get(uid), "headers": {"cache": "yes"}, "status": 200}
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
      cache.set(uid, enka_data, ttl=300)
      #返回数据，返回头，状态码
      return {"data": enka_data, "headers": {"cache": "no"}, "status": 200}

#验证uid
def verifyUid(uid):
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