from flask import Blueprint,redirect,request
import random as ran
import json
from var import log,img_source
import requests as r
# 创建一个蓝图对象
app = Blueprint('tool', __name__, url_prefix='/tool')
npcList = ['空', '荧', '派蒙', '纳西妲', '阿贝多', '温迪', '枫原万叶', '钟离', '荒泷一斗', '八重神子', '艾尔海森', '提纳里', '迪希雅', '卡维', '宵宫', '莱依拉', '赛诺', '诺艾尔', '托马', '凝光', '莫娜', '北斗', '神里绫华', '雷电将军', '芭芭拉', '鹿野院平藏', '五郎', '迪奥娜', '凯亚', '安柏', '班尼特', '琴', '柯莱', '夜兰', '妮露', '辛焱', '珐露珊', '魈', '香菱', '达达利亚', '砂糖', '早柚', '云堇', '刻晴', '丽莎', '迪卢克', '烟绯', '重云', '珊瑚宫心海', '胡桃', '可莉', '流浪者', '久岐忍', '神里绫人', '甘雨', '戴因斯雷布', '优菈', '菲谢尔', '行秋', '白术', '九条裟罗', '雷泽', '申鹤', '迪娜泽黛', '凯瑟琳', '多莉', '坎蒂丝', '萍姥姥', '罗莎莉亚', '留云借风真君', '绮良良', '瑶瑶', '七七', '奥兹', '米卡', '夏洛蒂', '埃洛伊', '博士', '女士', '大慈树王', '三月七', '娜塔莎', '希露瓦', '虎克', '克拉拉', '丹恒', '希儿', '布洛妮娅', '瓦尔特', '杰帕德', '佩拉', '姬子', '艾丝妲', '白露', '星', '穹', '桑博', '伦纳德', '停云', '罗刹', '卡芙卡', '彦卿', '史瓦罗', '螺丝咕姆', '阿兰', '银狼', '素裳', '丹枢', '黑塔', '景元', '帕姆', '可可利亚', '半夏', '符玄', '公输师傅', '奥列格', '青雀']
# 在蓝图对象上注册路由
@app.route("/yy/ys")
def ysyy():
  f = open("data/yy/ys.json",encoding="utf-8")
  ys = json.load(f)
  yyalldata = ys["data"]
  yynum = len(yyalldata)
  yyindex = ran.randint(0,yynum-1)
  log.debug("随机到的条目ID是：{}".format(yyindex))
  yydata = yyalldata[yyindex]
  log.debug(yydata)
  yydata["id"] = yyindex
  yyout = json.dumps(yydata,ensure_ascii=False)
  return yyout
@app.route("/img/ys")
def img_ys():
  
  imgSource_num = len(img_source)
  imgSource_index = ran.randint(0,imgSource_num-1)
  print(imgSource_index)
  imgSource_data = img_source[imgSource_index]
  if imgSource_data["type"] == "ftp":
    sourceConfig_url = imgSource_data["url"]+"/grc.json"
    sourceConfig = json.loads(r.get(sourceConfig_url).text)
    imgNum = sourceConfig["len"]
    imgIndex = ran.randint(1,imgNum)
    log.debug(sourceConfig)
    imgData = imgSource_data["url"] + sourceConfig["root"] + "/"+str(imgIndex) + "."+ sourceConfig["hj"]
    return redirect(imgData)
@app.route("/voice", methods=['POST'])
def voice():
  role = request.json.get("role")
  texts = request.json.get("text")
  log.debug(role)
  if role in npcList:
    textMax= 85*3
    textLen = len(texts)
    if textLen > textMax:
      return "Text too long",202
    else:
      voiceUrl = "https://genshinvoice.top/api?text={}&speaker={}".format(texts,role)
      return redirect(voiceUrl)
  else:
    return "The model is not currently supported or does not exist", 202
    