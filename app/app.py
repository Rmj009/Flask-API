# app = Flask(__name__)
# app.run(port=5000, debug=True)
# export DATABASE_URL='postgres://localhost:5432/
# import flask 
from flask import Flask
from flask import request, jsonify, escape
import sqlite3
app = Flask(__name__)
# app = flask.Flask(__name__)
app.config["DEBUG"] = True
# from .calculator import sum1
# #load_manuplate # ./../

from utils import ctest

import os
print(os.getcwd())
# from flask_sqlalchemy import SQLAlchemy

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/Flask-API'
# db = SQLAlchemy(app)


# @app.route('/user/<name>')
# def user_page(name):
#   return 'User: %s' % escape(name)

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d


#---------------------GET-----------------------
@app.route('/', methods=['GET'])
def home():
    return '''
<h1>{{ -- }}的个人主页</h1>
{% if bio %}
    <p>{{ bio }}</p>  {# 这里的缩进只是为了可读性，不是必须的 #}
{% else %}
    <p>自我介绍为空。</p>
{% endif %}  {# 大部分 Jinja 语句都需要声明关闭 #}
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route("/performance", methods=["GET"])
def performance():
  output_dict = {"success": False}
  if request.method == "GET":
      # query params
      arg_n = request.args.get('n')
      # body json
      body_json = request.get_json()
      print("body_json: ", body_json)
      print( body_json['jj'] )
      n =  ctest.sum1(arg_n) #nmp, trendObj = load_manpulate()
      print("n: ", n)
    #   print("trendObj: ", trendObj)
      return jsonify(output_dict), 200



# @app.route("/predict", methods=["POST"])
# def predict():
#   output_dict = {"success": False}  
#   if Flask.request.method == "POST":
#     data = Flask.request.json  # 讀取 json
#   return Flask.jsonify(output_dict), 200 # 回傳json, http status code


#-------ERROR Handling----------
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404



# app.run()
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)