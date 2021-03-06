from flask import Blueprint, render_template, current_app, jsonify

from app.views.api import api_bp
from app.views.page import page_bp

# 第一个参数是蓝图的名称，第二个参数是蓝图位置信息
myopia_bp = Blueprint('myopia', __name__,static_folder='app/static',static_url_path='')
myopia_bp.register_blueprint(api_bp, url_prefix='/api')
myopia_bp.register_blueprint(page_bp, url_prefix='/')


# @myopia_bp.get('/', defaults={'path': ''})
# @myopia_bp.get('/<path:path>/')
# def index(path):
#     return render_template('index.html')
