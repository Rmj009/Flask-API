# export DATABASE_URL='postgres://localhost:5432/
from flask import Flask
from datetime import datetime
from flask import request, jsonify, escape
from flask_sqlalchemy import SQLAlchemy             #import sqlite3
db = SQLAlchemy()
app = Flask(__name__)                               # app = flask.Flask(__name__) # coz, import style >>> import flask
app.config["DEBUG"] = True
from sqlalchemy import text


# --- import the others function/psql::db-migrator
# from . import db 
from utils import ctest                             # from .calculator import sum1 # #load_manuplate # ./../
import os
print(os.getcwd()) # print the pwd status
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:edge9527@localhost:5432/dev_tenant"
db.init_app(app)

class spc_measure_point_config(db.Model): #Sojourn
    __tablename__='spc_measure_point_config'
    uuid = db.Column(
        db.String(30),unique = True,  primary_key = True, nullable = False)
    name = db.Column(
        db.String(50), unique=False, nullable=False)
    # state = db.Column(
    #     db.String(30), unique=True, nullable=False)
    usl = db.Column(db.Integer, nullable=False)
    lsl = db.Column(db.Integer, nullable=False)
    std_value = db.Column(db.Integer, nullable=False)
    # description = db.Column(
    #     db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)



    def __init__(self,uuid,name,std_value,lsl,usl,create_time,update_time,work_oder_op_history_uuid,spc_measure_point_config_uuid):
        # route_uuid,,state,operation_uuid,measure_object_id
        self.uuid = uuid
        self.name = name
        self.std_value = std_value
        self.lsl = lsl
        self.usl = usl
        self.create_time = create_time
        self.update_time = update_time
        # self.state

class spc_measure_point_history(db.Model): #Sojourn
    __tablename__='spc_measure_point_history'
    uuid = db.Column(
        db.String(30),unique = True,  primary_key = True, nullable = False)
    work_oder_op_history_uuid = db.Column(
        db.String(50), unique=False, nullable=False)
    spc_measure_point_config_uuid = db.Column(
        db.String(50), unique=False, nullable=False)
    std_value = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)
    # description = db.Column(
    #     db.String(255), nullable=False)
    # state = db.Column(
    #     db.String(30), unique=True, nullable=False)



    def __init__(self,uuid,value,create_time,update_time,work_oder_op_history_uuid,spc_measure_point_config_uuid):
        # route_uuid,,state,operation_uuid,measure_object_id
        self.uuid = uuid
        self.value = value
        self.create_time = create_time
        self.update_time = update_time
        self.work_oder_op_history_uuid = work_oder_op_history_uuid
        self.spc_measure_point_config_uuid = spc_measure_point_config_uuid
        # self.state


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
@app.route('/test', methods=['GET'])
def index():
    # db.create_all()
    # Add data
    # testxxx = spc_measure_point_history('Max',8888,'', '', '','')
    # db.session.add(testxxx)
    # db.session.commit()
    #Read data
    query = spc_measure_point_history.query.filter_by(value = 12).first()
    print(query.value)
    # print(query.uuid)
    # sql_cmd =
    #     SELECT *
    #     FROM spc_measure_point_history

    # query_data = db.engine.execute(sql_cmd)
    # result = db.engine.execute(text("select * from work_order;").execution_options(autocommit=True))
    # print("result: ", result)
    return 'ok'


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

#-----Other module awaits--
# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d

# app.run()
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)