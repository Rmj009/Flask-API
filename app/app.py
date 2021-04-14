# export DATABASE_URL='postgres://localhost:5432/
from datetime import datetime
from flask import Flask, request, render_template, abort, url_for, json, jsonify, escape
from flask_sqlalchemy import SQLAlchemy
import json
import html          #import sqlite3
db = SQLAlchemy()
app = Flask(__name__, static_url_path='')   # app = flask.Flask(__name__) # coz, import style >>> import flask
app.config["DEBUG"] = True
from sqlalchemy.sql import text
"""
import the others function
"""
# from . import db 
# from utils import ctest
from calculator import *  #load_manuplate # ./../
from spcchart import *
import os,sys,traceback
from sqlalchemy import create_engine 
###########CONFIGURATION###################
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

class PassGateway():
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
    # while cannot show the web-page, and print out following tips
    def page_not_found(e):
        return "<h1>404</h1><p> <bold>4040404040</bold> </p>", 404

    def abort_msg(e):
        """500 bad request for exception

        Returns:
            500 and msg which caused problems
        """
        error_class = e.__class__.__name__ # 引發錯誤的 class
        detail = e.args[0] # 得到詳細的訊息
        cl, exc, tb = sys.exc_info() # 得到錯誤的完整資訊 Call Stack
        lastCallStack = traceback.extract_tb(tb)[-1] # 取得最後一行的錯誤訊息
        fileName = lastCallStack[0] # 錯誤的檔案位置名稱
        lineNum = lastCallStack[1] # 錯誤行數 
        funcName = lastCallStack[2] # function 名稱
        # generate the error message
        errMsg = "Exception raise in file: {}, line {}, in {}: [{}] {}. Please contact whom in charge of project!".format(fileName, lineNum, funcName, error_class, detail)
        # return 500 code
        abort(500, errMsg)

    #-----Other module awaits--
    #############################
    ######Factory module#########
    #############################
    # def dict_factory(cursor, row):
        # d = {}
        # for idx, col in enumerate(cursor.description):
        #     d[col[0]] = row[idx]
        # return d

#----------------GET-------------------
@app.route('/query', methods=['GET'])
def index():
    # sql_cmd = (
    #     '''
    # SELECT spc_measure_point_config.name, spc_measure_point_history.value,(spc_measure_point_config.usl+spc_measure_point_config.std_value) AS USL, (spc_measure_point_config.std_value-spc_measure_point_config.lsl) AS LSL --,spc_measure_point_history.measure_object_id

    # FROM spc_measure_point_config  left OUTER JOIN spc_measure_point_history
    # ON spc_measure_point_config.uuid = spc_measure_point_history.spc_measure_point_config_uuid

    # WHERE spc_measure_point_history.value NOT IN (-88888888)

    # order by spc_measure_point_config.uuid;
    #     '''  
    # )
    sql_cmd = (
        """
        SELECT value FROM spc_measure_point_history
        WHERE value NOT IN (-88888888);
        """
    )
    # test()
    # result = db.engine.execute(text("sql_cmd").execution_options(autocommit=True))
    # print("result: ", result)
    # # user = db.session.query().from_statement(text(sql_cmd)).params(name="").all()
    # method_a starts a transaction and calls method_b
    def method_a(connection):
        with connection.begin():  # open a transaction
            method_b(connection)

    # method_b also starts a transaction
    def method_b(connection):
        with connection.begin(): # open a transaction - this runs in the context of method_a's transaction
            connection.execute(sql_cmd)
    

    # # result = connection.execute(sql_cmd).first()[0]
    resultproxy = engine.execute(sql_cmd)
    d = [{column: value for column, value in row.items()} for row in resultproxy] # fetch all value
    # d, a = {}, []
    # for row in resultproxy:
    # # row.items() returns an array like [(key0, value0), (key1, value1)]
    #     for column, value in row.items():
    #     # build up the dictionary
    #         d = {**d, **{column: value}}
    #     a.append(d)
    print("sql result: ",d)
    
    return 'ok', #,result #,id_count #query_data #

@app.route("/perform", methods=['GET'])
def perform():
  output_dict = {"success": False}
  if request.method == "GET":
      # query params
    #   arg_n = request.args.get('n') # try to request 'n'
      # body json
      body_json = request.get_json() #index() get the json from body
      paul = body_json['paul']

      u = body_json['upperLimit']
      l = body_json['lowerLimit']
      v = body_json['value']
      test_u_l(u, l, v)
      if v > u:
        print("no 1")
      elif v < l:
        print("no 2")
      else:
        print("ok")
      
      print("paul: ",paul)
      print("body_json: ", body_json)
    #   print( body_json['jj'] )
    #   n =  ctest.sum1(arg_n) #nmp, trendObj = load_manpulate()
    #   print("n: ", n)
    #   print("trendObj: ", trendObj)
      return body_json #jsonify(index()), 200



# mylst = [2 for i in range(100)]
mylst = np.linspace(1,100,30)
usl = 18
lsl = 10
results = calc(mylst, usl, lsl) # print(results)
resultD = dict(zip(keys, results)) # results turn into dict type
index()
#-----------------ENTRANCE-----------------------
@app.route('/', methods=['GET'])
def home():
    try: 
        return user,render_template('index.html', title="page", jsonfile=json.dumps(resultD)) #{"test": 123}
    except Exception as e:
        abort_msg(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

