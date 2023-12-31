from flask import Flask, request, redirect, make_response #导入Flask框架
from var import conf,log, req_id,conf
from logging import getLogger #用于关闭Flask日志
from views import tool,ys,dev,sr #导入视图函数
import cli
req_num = 0
req_ids = ""
#关闭flask日志
flog = getLogger('werkzeug')
flog.disabled = True
#初始化Flask
app = Flask(__name__)
#注册蓝图
app.register_blueprint(tool.app)
app.register_blueprint(ys.app)
app.register_blueprint(sr.app)
app.register_blueprint(dev.app)
app.register_blueprint(cli.bp)
if conf["log.level"] == "DEBUG":
    mode = True
else:
    mode = False

@app.before_request
def before_request():
    global req_num
    global req_ids
    req_num = req_num+1
    if conf["CDN"] == "":
      ip = request.remote_addr
    else:
      head = conf["CDN"]
      ip = request.headers[head]
    req_method = request.method
    req_path = request.path
    UA = request.headers.get("User-Agent")
    #输出日志
    log.info("---------------------------")
    log.info("请求IP：{}".format(ip))
    log.info("请求方法：{}".format(req_method))
    log.info("请求路径：{}".format(req_path))
    log.info("请求ID：{}".format(req_id(req_num)))
    log.info("请求UA：{}".format(UA))
    log.info("第{}次请求".format(req_num))
@app.after_request
def set_response_headers(response):
    global req_ids
    req_id = req_ids
    response.headers['GSAPI-Version'] = conf["version"]
    response.headers['GSAPI-Request-ID'] = req_id
    # response.headers[]
    # 添加更多的响应头设置
    return response
  
  
#主页
@app.route("/")
def index():
  return redirect(conf["index"], code=301)

#GIT存储库
@app.route("/git")
def git():
  return redirect(conf["git"], code=301)
#文档
@app.route("/docs")
def docs():
  return redirect(conf["docs"], code=301)
if __name__ == '__main__':
    app.run(host=conf["host"], port=int(conf["port"]), debug=mode)

