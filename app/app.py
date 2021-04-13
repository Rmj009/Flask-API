# export DATABASE_URL='postgres://localhost:5432/
from datetime import datetime
from flask import Flask, request, render_template, abort, url_for, json, jsonify, escape
from flask_sqlalchemy import SQLAlchemy
import json
import html          #import sqlite3
db = SQLAlchemy()
app = Flask(__name__,  static_url_path='')                               # app = flask.Flask(__name__) # coz, import style >>> import flask
app.config["DEBUG"] = True
from sqlalchemy import text


# --- import the others function/psql::db-migrator
# from . import db 
# from utils import ctest
from .calculator import perform # #load_manuplate # ./../
from spcchart import *
import os

from sqlalchemy import create_engine 
print(os.getcwd()) # print the pwd status
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:edge9527@localhost:5432/dev_tenant"
engine = create_engine('postgresql://postgres:edge9527@localhost:5432/dev_tenant')
connection = engine.connect()
db.init_app(app)


def test():
    print("kkk")

def test_u_l(u, l, v):
    print('lol....')
    if v > u:
        print("no 1")
    elif v < l:
        print("no 2")
    else:
        print("ok")

#---------------------GET-----------------------

@app.route('/test', methods=['GET'])
def index():

    test()

    result = db.engine.execute(text("select value FROM spc_measure_point_history;").execution_options(autocommit=True))
    print("result: ", result)

    results = connection.execute('select value FROM spc_measure_point_history;')
    id_count = results.first()[0]
    # sql_cmd = (
    #     '''
    # SELECT spc_measure_point_config.name, spc_measure_point_history.value,(spc_measure_point_config.usl+spc_measure_point_config.std_value) AS USL, (spc_measure_point_config.std_value-spc_measure_point_config.lsl) AS LSL --,spc_measure_point_history.measure_object_id

    # FROM spc_measure_point_config  left OUTER JOIN spc_measure_point_history
    # ON spc_measure_point_config.uuid = spc_measure_point_history.spc_measure_point_config_uuid

    # WHERE spc_measure_point_history.value NOT IN (-88888888)

    # order by spc_measure_point_config.uuid
    #     '''
    # )
    # query_data = db.engine.execute(sql_cmd)
    # resultproxy = db_session.execute(query_data)
    # # [{column: value for column, value in rowproxy.items()} for rowproxy in resultproxy]
    # d, a = {}, []
    # for rowproxy in resultproxy:
    # # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
    #     for column, value in rowproxy.items():
    #     # build up the dictionary
    #         d = {**d, **{column: value}}
    #     a.append(d)
    # print("sql result: ", query_data)

    return 'ok', result, #query_data #,id_count


@app.route("/performance", methods=['GET'])
def performance():
  output_dict = {"success": False}
  if request.method == "GET":
      # query params
      arg_n = request.args.get('n')
      # body json
      body_json = request.get_json() #index() get the json from body
      paul = body_json['paul']

      u = body_json['upperLimit']
      l = body_json['lowerLimit']
      v = body_json['value']
      test_u_l(u, l, v)
    #   if v > u:
    #     print("no 1")
    #   elif v < l:
    #     print("no 2")
    #   else:
    #     print("ok")
      
      print("paul: ",paul)
      print("body_json: ", body_json)
    #   print( body_json['jj'] )
    #   n =  ctest.sum1(arg_n) #nmp, trendObj = load_manpulate()
    #   print("n: ", n)
    #   print("trendObj: ", trendObj)
      return body_json #jsonify(index()), 200



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return do_the_login()
#     else:
#         return show_the_login_form()

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

#-----Other module awaits--
# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', title="page", jsonfile=json.dumps({"test": 123}))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

