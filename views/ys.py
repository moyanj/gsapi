from flask import Flask, Blueprint, request
from lib import viewFun
app = Blueprint('ys', __name__, url_prefix='/ys')
#获取玩家昵称
@app.route("/name")
def uid():
  tmp3 = viewFun(request)
  if tmp3["status"] == 201 or tmp3["status"] == 202:
    return tmp3["data"], tmp3["status"], tmp3["headers"]
  else:
    tmp = tmp3["data"]
    tmp2 = tmp["playerInfo"]
    return tmp2["nickname"], tmp3["status"], tmp3["headers"]

#获取玩家冒险等阶
@app.route("/level")
def level():
  
  tmp0 = viewFun(request)
  if tmp0["status"] == 201 or tmp0["status"] == 202:
    return tmp0["data"], tmp0["status"], tmp0["headers"]
  else:
    tmp = tmp0["data"]
    tmp2 = tmp["playerInfo"]
    return str(tmp2["level"]), tmp0["status"], tmp0["headers"]

#获取玩家世界等级
@app.route("/wl")
def worldLevel():
  tmp0 = viewFun(request)
  if tmp0["status"] == 201 or tmp0["status"] == 202:
    return tmp0["data"], tmp0["status"], tmp0["headers"]
  else:
    tmp = tmp0["data"]
    tmp2 = tmp["playerInfo"]
    return str(tmp2["worldLevel"]), tmp0["status"], tmp0["headers"]

#获取玩家签名
@app.route("/sign")
def sign():
  tmp0 = viewFun(request)
  if tmp0["status"] == 201 or tmp0["status"] == 202:
    return tmp0["data"], tmp0["status"], tmp0["headers"]
  else:
    tmp = tmp0["data"]
    tmp2 = tmp["playerInfo"]
    return tmp2["signature"], tmp0["status"], tmp0["headers"]

#获取玩家深渊
@app.route("/abyss")
def abyss():
  tmp0 = viewFun(request)
  if tmp0["status"] == 201 or tmp0["status"] == 202:
    return tmp0["data"], tmp0["status"], tmp0["headers"]
  else:
    tmp = tmp0["data"]
    tmp2 = tmp["playerInfo"]
    a = tmp2["towerFloorIndex"]
    b = tmp2["towerLevelIndex"]
    c = "{}-{}".format(a, b)
    return c, tmp0["status"], tmp0["headers"]

#获取玩家间数
@app.route("/abyss/room")
def abyss_room():
  tmp0 = viewFun(request)
  if tmp0["status"] == 201 or tmp0["status"] == 202:
    return tmp0["data"], tmp0["status"], tmp0["headers"]
  else:
    tmp = tmp0["data"]
    tmp2 = tmp["playerInfo"]
    b = str(tmp2["towerLevelIndex"])
    return b, tmp0["status"], tmp0["headers"]

#获取玩家层数
@app.route("/abyss/floor")
def abyss_floor():
  tmp0 = viewFun(request)
  if tmp0["status"] == 201 or tmp0["status"] == 202:
    return tmp0["data"], tmp0["status"], tmp0["headers"]
  else:
    tmp = tmp0["data"]
    tmp2 = tmp["playerInfo"]
    b = str(tmp2["towerFloorIndex"])
    return b, tmp0["status"], tmp0["headers"]
  #return tmp

#获取玩家成就数量
@app.route("/achieve")
def achieve():
  tmp0 = viewFun(request)
  if tmp0["status"] == 201 or tmp0["status"] == 202:
    return tmp0["data"], tmp0["status"], tmp0["headers"]
  else:
    tmp = tmp0["data"]
    tmp2 = tmp["playerInfo"]
    b = str(tmp2["finishAchievementNum"])
    return b, tmp0["status"], tmp0["headers"]
