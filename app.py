from flask import Flask, request,redirect #导入Flask框架
from var import conf,log, req_id
from logging import getLogger #用于关闭Flask日志
from views import tool,ys,admin #导入视图函数
req_num = 0
#关闭flask日志
flog = getLogger('werkzeug')
flog.disabled = True
#初始化Flask
app = Flask(__name__)

#注册蓝图
app.register_blueprint(tool.app)
app.register_blueprint(ys.app)
app.register_blueprint(admin.app)

@app.before_request
def before_request():
    global req_num
    req_num = req_num+1
    if conf["CDN"] == "":
      ip = request.remote_addr
    else:
      head = conf["CDN"]
      ip = request.headers[head]
    req_method = request.method
    req_path = request.path
    log.info("---------------------------")
    log.info("请求IP：{}".format(ip))
    log.info("请求方法：{}".format(req_method))
    log.info("请求路径：{}".format(req_path))
    log.info("请求ID：{}".format(req_id(req_num)))
    

  
  
#主页
@app.route("/")
def index():
  return redirect(conf["index"], code=301)

@app.route("/git")
def git():
  return redirect(conf["git"], code=301)

@app.route("/docs")
def gti():
  return redirect(conf["index"], code=301)

app.run(host=conf["host"], port=conf["port"], debug=False)

