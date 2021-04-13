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

class spc_measure_point_config(db.Model): #Sojourn
    __tablename__='spc_measure_point_config'
    uuid = db.Column(
        db.String(30),unique = True,  primary_key = True, nullable = False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)
    route_uuid = db.Column(
        db.String(50), unique=False, nullable=False)
    operation_uuid = db.Column(
        db.String(50), unique=False, nullable=False)
    route_operation_uuid = db.Column(
        db.String(50), unique=False, nullable=False)
    tenant_id = db.Column(
        db.String(50), unique=False, nullable=False)
    name = db.Column(
        db.String(50), unique=False, nullable=False)
    description = db.Column(
        db.String(255), nullable=False)
    unit = db.Column(
        db.String(8), unique=False, nullable=False)
    mode = db.Column(
        db.String(8), unique=False, nullable=False)
    std_value = db.Column(db.Integer, nullable=False)
    usl = db.Column(db.Integer, nullable=False)
    lsl = db.Column(db.Integer, nullable=False)
    measure_amount = db.Column(db.Integer, nullable=False)
    range_spec = db.Column(db.Integer, nullable=False)
    sample_number = db.Column(db.Integer, nullable=False)
    rules = db.Column(
        db.String(64), nullable=False)
    # state = db.Column(
    #     db.String(30), unique=True, nullable=False)

    def __init__(
        self,uuid,create_time,update_time,route_uuid,operation_uuid,
        route_operation_uuid,tenant_id,name,description,unit,mode,std_value,lsl,usl,
        measure_amount,range_spec,sample_number,rules):
        self.uuid = uuid
        self.create_time = create_time
        self.update_time = update_time
        self.route_uuid = route_uuid
        self.operation_uuid = operation_uuid
        self.route_operation_uuid = route_operation_uuid
        self.tenant_id = tenant_id
        self.name = name
        self.description = description
        self.unit = unit
        self.mode = mode
        self.std_value = std_value
        self.lsl = lsl
        self.usl = usl
        self.measure_amount = measure_amount
        self.range_spec = range_spec
        self.sample_number = sample_number
        self.rules = rules
        # self.state

class spc_measure_point_history(db.Model): #Sojourn
    __tablename__='spc_measure_point_history'
    uuid = db.Column(
        db.String(30),unique = True,  primary_key = True, nullable = False)
    work_oder_op_history_uuid = db.Column(
        db.String(50), unique=False, nullable=False)
    tenant_id = db.Column(
        db.String(50), unique=False, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)
    worker_id = db.Column(
        db.String(50), unique=False, nullable=False)
    spc_measure_point_config_uuid = db.Column(
        db.String(50), unique=False, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    measure_object_id = db.Column(db.Integer, nullable=False)
    spc_measure_instrument_uuid = db.Column(
        db.String(50), unique=False, nullable=False)
    # state = db.Column(
    #     db.String(30), unique=True, nullable=False)
    
    def __init__(self,uuid,value,create_time,update_time,work_oder_op_history_uuid,spc_measure_point_config_uuid):
        # route_uuid,,state,operation_uuid,measure_object_id
        self.uuid = uuid
        self.work_oder_op_history_uuid = work_oder_op_history_uuid
        self.tenant_id = tenant_id
        self.create_time = create_time
        self.update_time = update_time
        self.worker_id = worker_id
        self.spc_measure_point_config_uuid = spc_measure_point_config_uuid
        self.value = value
        self.measure_object_id = measure_object_id
        self.spc_measure_instrument_uuid = spc_measure_instrument_uuid
        # self.state

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

