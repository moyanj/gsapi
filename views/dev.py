from flask import Blueprint, request, jsonify
import json
# 创建一个蓝图对象
app = Blueprint('admin', __name__, url_prefix='/dev')

# 在蓝图对象上注册路由
@app.route("/conf")
def conf():
    # 加载配置文件
    with open('data/config.json', 'r') as file:
        config = json.load(file)
    # 删除敏感信息
    del config['chat']['token']
    del config["cookie"]["key"]
    # 返回更新后的配置
    return jsonify(config)