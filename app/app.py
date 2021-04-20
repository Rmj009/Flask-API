# export DATABASE_URL='postgres://localhost:5432/
from datetime import datetime
from flask import Flask, request, render_template, abort, url_for, redirect, json, jsonify, escape
from flask_sqlalchemy import SQLAlchemy
import json,html
app = Flask(__name__, static_url_path='') # coz, import style >>> import flask
# from sqlalchemy.sql import text
"""
import the others function
"""
import spcchart
from calculator import *
from spcTable import *
import os,sys,traceback
from sqlalchemy import create_engine 
#------------CONFIGURATION--------------
# print(os.getcwd()) # print the pwd status
class PassGateway():
  #-------ERROR Handling----------
  """
  500 bad request for exception
  Returns:
  500 and msg which caused problems
  """
  @app.errorhandler(404)  # while cannot show the web-page, and print out following tips
  def page_not_found(e):
    return "<h1>404</h1><p> <bold>4040404040</bold> </p>", 404

  def abort_msg(e):
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
#----------------GET-------------------
@app.route('/query', methods=['GET'])
def index():
    if request.method == "GET":
      # query params
    #   arg_n = request.args.get('n') # try to request 'n'
      # body json
      body_json = request.get_json() # get the json from body
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
    return 'ok' #,result

@app.route("/capability", methods=['GET'])
def capability():
  #  username = request.args.get('username')
  #  password = request.args.get('password')
    usl = 100 # concatenate the user query
    lsl = 10 #吃資料庫usl lsl 
    keys = ["Cp","Cpu","Cpk","Ppk"]
    resultCapablity = dict(zip(keys, calc(mylst = queryfunc(), usl=usl, lsl=lsl)))
  # map(dict, map(lambda t:zip(('num','char'),t), zip(list_nums,list_chars))) # [values for key,values in d.items()]
    print("Capablity result: ", resultCapablity)
    # resultImage = plotQuery()
    return resultCapablity #,jsonify(resultCapablity), 200
#-----------------ENTRANCE-----------------------
@app.route('/', methods=['GET'])
def home():
    try: 
        return render_template('index.html', title="spc_show", jsonfile=json.dumps(capability()()) )
    except Exception as e:
        pass


@app.route('/loginQ', methods=['GET', 'POST']) 
def loginQ():
    if request.method == 'POST': 
        return 'SpcDashboard ' + request.values['specificChart'] #redirect(url_for('hello', specificChart=request.form.get('specificChart')))
    # return render_template('loginQ.html')

    return "<form method='post' action='/loginQ'><input type='text' name='specificChart' />" \
            "</br>" \
           "<button type='submit'>Submit</button></form>"

# @app.route('/hello/<specificChart>')
# def hello(specificChart):
#     return render_template('helloDashboard.html', username=specificChart)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
