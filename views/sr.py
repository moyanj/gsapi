from flask import Blueprint
app = Blueprint('my_bp', __name__,url_prefix="/sr")
@app.route('/')
def index():
    return "This is the query API for StarRail."