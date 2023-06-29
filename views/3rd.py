from flask import Blueprint
app = Blueprint('3rd', __name__,url_prefix="/3rd")
@app.route('/')
def index():
    return 'Hello, World!'