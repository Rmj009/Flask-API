# export DATABASE_URL='postgres://localhost:5432/
from datetime import datetime
from flask import Flask, request, render_template, abort, url_for, json, jsonify, escape
from flask_sqlalchemy import SQLAlchemy
import json
import html          #import sqlite3
# db = SQLAlchemy()
# app = Flask(__name__, static_url_path='')   # app = flask.Flask(__name__) # coz, import style >>> import flask
# app.config["DEBUG"] = True
# from sqlalchemy.sql import text
"""
import the others function
"""
from spcchart import *
from spcTable import *
from calculator import *
import os,sys,traceback
from sqlalchemy import create_engine 
#------------CONFIGURATION--------------
# print(os.getcwd()) # print the pwd status
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
    # test()
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
    return #'ok', #,result

@app.route("/perform", methods=['GET'])
def perform():
    # resultD = qquery()
    usl = 10
    lsl = 10
#   = np.linspace(1,30,30)
    resultA = calc(mylst = qquery(), usl=usl, lsl=lsl) ; keys = ["Cp","Cpu","Cpk","Ppk"]
    resultD = dict(zip(keys, resultA))  #resultA turn into dict type
  # map(dict, map(lambda t:zip(('num','char'),t), zip(list_nums,list_chars))) # [values for key,values in d.items()]
    print("sql result: ", resultD)
    return jsonify(resultD), 200
#-----------------ENTRANCE-----------------------
@app.route('/', methods=['GET'])
def home():
    try: 
        return render_template('index.html', title="page", jsonfile=json.dumps(perform())) #{"test": 123}
    except Exception as e:
        pass
        # abort_msg(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
