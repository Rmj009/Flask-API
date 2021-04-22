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
    # query params
    global spcTable_query
    b = request.args.get('begin_time') # try to request 'n'
    e = request.args.get('expiry_time')
    wuuid = request.args.get('wooh_uuid')
    suuid = request.args.get('smpc_uuid')
    resultCapablity = spcTable.queryfunc(begin_time=b,expiry_time=e,wooh_uuid=wuuid,smpc_uuid=suuid)
    # resultCapablity = dict(zip(keys, calc(mylst = spcTable_quesuuidry)))
    print("Capablity result: ", resultCapablity)

    return resultCapablity


#-----------------ENTRANCE-----------------------
@app.route('/', methods=['GET'])
def home():
  b = request.args.get('begin_time') # b = 2020-09-02T07:41:03Z
  e = request.args.get('expiry_time') # e = 2021-01-15T10:47:32Z
  wuuid = request.args.get('wooh_uuid')
  suuid = request.args.get('smpc_uuid')
  # b = '2020-09-02T07:41:03Z'
  # e = '2021-01-15T10:47:32Z'
  # wuuid = 'd5473fb7-42ac-4794-bf4d-358f4ddccd1c'
  # suuid = '69636a46-48cb-4a99-976e-5ecc024c1332'
  resultCapablity = spcTable.queryfunc(begin_time=b,expiry_time=e,wooh_uuid=wuuid,smpc_uuid=suuid)
  # print("Capablity result: ", resultCapablity)
  try: 
      return render_template('index.html', title="spc_show", jsonfile=json.dumps(resultCapablity) )
  except Exception as e:
      pass


@app.route('/loginQ', methods=['GET', 'POST']) 
def loginQ():
    if request.method == 'POST': 
        return 'SpcDashboard ' + request.values['specificChart'] #redirect(url_for('hello', specificChart=request.form.get('specificChart')))
    # return render_template('loginQ.html')
    #  username = request.args.get('username')
    #  password = request.args.get('password')

    return "<form method='post' action='/loginQ'><input type='text' name='specificChart' />" \
            "</br>" \
           "<button type='submit'>Submit</button></form>"

# @app.route('/hello/<specificChart>')
# def hello(specificChart):
#     return render_template('helloDashboard.html', username=specificChart)



def test():
 return calc(mylst)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
