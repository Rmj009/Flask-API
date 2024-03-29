from flask import Flask, request, render_template, abort, url_for, json, jsonify, escape
from sqlalchemy import select, column, join, create_engine
from sqlalchemy.orm import sessionmaker, aliased
from calculator import *
from nelsonRules import *
from alchemy_db import *
import threading
import os
db = SQLAlchemy() # db.init_app(app)
engine = create_engine('postgresql://postgres:edge9527@localhost:5432/dev_tenant')
# engine = create_engine(os.getenv('PG_URL'))

Session = sessionmaker(bind=engine)
# create a configured "Session" class
session = Session() # create a Session
connection = engine.connect()

"""
# app.config['SQLALCHEMY_DATABASE_URI'] = [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]

Definition of the table format
1. spc_measure_point_config
2. spc_measure_point_history

user params input: 
* spc_measure point config UUID, work order op history uuid
* startTime 開工 
* endTime 完工
python output:
cpl,cp,cpk,ppk,..
"""
#-----------------------------------------------
class SpcTable:
    def __init__(self,rule):
        self.rule = rule
        self.array = array        
    # self.firstvar = startTime
    # self.lastvar = endTime
    def dataPipline(tables):
        valuelst = [item[0] for item in tables]
        print("vvvv:", valuelst)
        goodlst = [item[1] for item in tables]
        defectlst = [item[2] for item in tables]
        lslspec = [item[3] for item in tables][0]
        print("####lslspec###", lslspec)
        uslspec = [item[4] for item in tables][0]
        qResult = {"valuelst":valuelst,"goodlst":goodlst ,"defectlst":defectlst ,"lslspec": lslspec,"uslspec": uslspec}
        return qResult

    def drawchart1(datapoints):
        #---------invoke western------------
        # datapoints = valuelst
        trendObj = {'all_vals': datapoints,'format_1': np.zeros(len(datapoints)),'format_2': np.zeros(len(datapoints)),'format_3': np.zeros(len(datapoints)),'format_4': np.zeros(len(datapoints))}
        print("pppppppppp",trendObj['all_vals'])
        # assign_datum(obj = trendObj, datum = 10)
        def format_arr(rule):
            rule_arr = 'format_' + str(rule)
            return [index for index,val in enumerate(trendObj[rule_arr]) if val]
        def plotAxlines(array):
            theMean = np.mean(array)
            sd = np.std(array)
            colors = ['black','green','violet','red']
            for level,color in enumerate(colors):
                upper = theMean + sd*level
                lower = theMean - sd*level
                plt.axhline(y=upper, linewidth=0.5, color=color)
                plt.axhline(y=lower, linewidth=0.5, color=color)
            return
        mark = 3.5
        plt.figure(figsize=(60,30))
        plt.plot(trendObj['all_vals'], color='red',markevery=format_arr(1), ls="", marker='s',mfc = 'none', mec='red', label="Rule1", markersize=mark*1.5)
        plt.plot(trendObj['all_vals'], color='blue',markevery=format_arr(2), ls="", marker='o', mfc='none',mec='blue',label="Rule2", markersize=mark*1)
        plt.plot(trendObj['all_vals'], color='brown',markevery=format_arr(3), ls="", marker='o', mfc='none',mec='brown',label="Rule3", markersize=mark*1.5)
        plt.plot(trendObj['all_vals'], color='blue',markevery=format_arr(4), ls="", marker='s', mfc='none',mec='green',label="Rule4", markersize=mark*1.0)
        plt.plot(trendObj['all_vals'], color='#81B5CB', ls="", marker=".", markersize=mark)
        plotAxlines(trendObj['all_vals'])
        plt.legend()
        plt.ylim(0,25)
        # # plt.plot(datapoints)
        plt.savefig('static/control-chart.png')
        # # g = sns.relplot(x = 'all_vals', y = 'format_1', data = trendObj, kind="line")
        # # g.fig.autofmt_xdate()
        plt.show()


    def drawchart2(datapoints):
        # apply_rules(dataPipline(tables = )
        pass
    # start_time,end_time,work_order_op_history_uuid,spc_measure_point_config_uuid
    def queryfunc(startTime,endTime,wooh_uuid,smpc_uuid): 
        table_config = aliased(spc_measure_point_config) # operation_uuid <=> table_work_order
        table_history = aliased(spc_measure_point_history) # work_order_op_history_uuid <=> table_work_order.uuid
        table_work_order = aliased(work_order_op_history) # operation_uuid <=> table_config
        try:
            table_history.work_order_op_history_uuid = wooh_uuid
            j1 = session.query(table_history.value,table_work_order.good,table_work_order.defect,table_config.lsl,table_config.usl)\
            .join(table_config, table_history.spc_measure_point_config_uuid == table_config.uuid)\
            .join(table_work_order, table_work_order.uuid == table_history.work_order_op_history_uuid)\
            .where((table_work_order.start_time > startTime) & (table_work_order.end_time < endTime) & (table_history.spc_measure_point_config_uuid == smpc_uuid))
            if (table_history.work_order_op_history_uuid != None) :
                yy = j1.filter(table_history.work_order_op_history_uuid == wooh_uuid)
            queryResult = [row for row in session.execute(yy)]
            print("####",queryResult,sep='\n')
            qResult = SpcTable.dataPipline(tables=queryResult)
            # print("qqqqqqqqqqqqqq",qResult['valuelst'])
            # SpcTable.drawchart2(datapoints = qResult['valuelst'])
            try:
                # t = threading.Thread(target = apply_rules, args=(qResult['valuelst'],'all',2) ,daemon=True)
                
                resultCapablity = Calculator.calc(mylst = qResult)
                print('resultCCCC:',resultCapablity)
            except Exception as e:
                print("chart error", e)
            
            return resultCapablity#, t.start()

        except Exception as e:
                print("error type: ",type(e),str(e))
                raise
        
  
    # stmt = select(table_history).select_from(j1) #subquery
    # print("stmt:", stmt)
    # print(stmt)

    # QQ = session.query(table_history.value,table_config).join(table_history, table_history.spc_measure_point_config_uuid == table_config.uuid).filter(table_history.spc_measure_point_config_uuid == '57016b97-2355-460f-b673-6512d8ed00da')
    # print(QQ)
    # sql轉譯



# if __name__ == "__main__":

# #     db = SQLAlchemy()
# #     app = Flask(__name__, static_url_path='')   # app = flask.Flask(__name__) # coz, import style >>> import flask
# #     app.config["DEBUG"] = True
# #     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# #     app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:edge9527@localhost:5432/dev_tenant"
# #     engine = create_engine('postgresql://postgres:edge9527@localhost:5432/dev_tenant')
# #     Session = sessionmaker(bind=engine)
# #     # create a configured "Session" class
# #     session = Session() # create a Session
# #     connection = engine.connect()
# #     db.init_app(app)
#     print("###open###1111")
#     b = '2020-09-02T07:41:03Z'
#     e = '2021-01-15T10:47:32Z'
#     wuuid = 'd5473fb7-42ac-4794-bf4d-358f4ddccd1c'
#     suuid = '69636a46-48cb-4a99-976e-5ecc024c1332'
#     resultCapablity = SpcTable.queryfunc(startTime=b,endTime=e,wooh_uuid=wuuid,smpc_uuid=suuid)
#     print(resultCapablity)
