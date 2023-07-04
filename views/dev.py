from flask import Blueprint, request, jsonify
import json
# 创建一个蓝图对象
app = Blueprint('admin', __name__, url_prefix='/dev')

