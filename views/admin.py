from flask import Blueprint, request

# 创建一个蓝图对象
app = Blueprint('admin', __name__, url_prefix='/admin')

# 在蓝图对象上注册路由
@app.get("/cache")
def del_cache():
  
  password = request.values.get("pass")
  if password == "jdc2010":
    cache.delete_all()
    return "ok"
  else:
    return "no admin"
