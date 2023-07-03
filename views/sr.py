from flask import Flask, Blueprint, request
from fun import req_eli
app = Blueprint('sr', __name__,url_prefix="/sr")
@app.route('/')
def index():
    return "This is the query API for StarRail."

@app.route("/all")
def all():
  uid = request.values.get("uid")
  req = req_eli(uid)
  if req["status"] == 201 or req["status"] == 202:
    return req["data"], req["status"], req["headers"]
  else:
    allData = req["data"]
    tmp2 = allData["playerDetailInfo"]
    returnData = {
        "nickName":tmp2["nickname"],
        "level":tmp2["level"],
        "WL":tmp2["worldLevel"],
        "sign":tmp2["signature"],
        "birthday":tmp2["birthday"],
        "friend":tmp2["friendCount"]
    }
    return returnData, req["status"], req["headers"]
#获取玩家昵称
@app.route("/name")
def uid():
  uid = request.values.get("uid")
  req = req_eli(uid)
  if req["status"] == 201 or req["status"] == 202:
    return req["data"], req["status"], req["headers"]
  else:
    tmp = req["data"]
    tmp2 = tmp["playerDetailInfo"]
    return tmp2["nickname"], req["status"], req["headers"]

#获取玩家冒险等阶
@app.route("/level")
def level():
  uid = request.values.get("uid")
  req = req_eli(uid)
  if req["status"] == 201 or req["status"] == 202:
    return req["data"], req["status"], req["headers"]
  else:
    tmp = req["data"]
    tmp2 = tmp["playerDetailInfo"]
    return str(tmp2["level"]), req["status"], req["headers"]

#获取玩家世界等级
@app.route("/wl")
def worldLevel():
  uid = request.values.get("uid")
  req = req_eli(uid)
  if req["status"] == 201 or req["status"] == 202:
    return req["data"], req["status"], req["headers"]
  else:
    tmp = req["data"]
    tmp2 = tmp["playerDetailInfo"]
    return str(tmp2["worldLevel"]), req["status"], req["headers"]

#获取玩家签名
@app.route("/sign")
def sign():
  uid = request.values.get("uid")
  req = req_eli(uid)
  if req["status"] == 201 or req["status"] == 202:
    return req["data"], req["status"], req["headers"]
  else:
    tmp = req["data"]
    tmp2 = tmp["playerDetailInfo"]
    return tmp2["signature"], req["status"], req["headers"]
    
@app.route("/role")
def role():
    return "HelloWorld"

@app.route("/role/<id>")
def role_info(id):
    return "HelloWorld"
