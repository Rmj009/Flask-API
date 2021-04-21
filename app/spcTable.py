from flask import Flask, request, render_template, abort, url_for, json, jsonify, escape
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import text
from sqlalchemy.sql import text
from sqlalchemy import select,column,join
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, aliased
db = SQLAlchemy()
app = Flask(__name__, static_url_path='')   # app = flask.Flask(__name__) # coz, import style >>> import flask
app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:edge9527@localhost:5432/dev_tenant"
engine = create_engine('postgresql://postgres:edge9527@localhost:5432/dev_tenant')
Session = sessionmaker(bind=engine)
# create a configured "Session" class
session = Session() # create a Session
connection = engine.connect()
db.init_app(app)
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
class spc_measure_point_config(db.Model): #Sojourn 1
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
    std_value = db.Column(db.Float, nullable=False)
    usl = db.Column(db.Float, nullable=False)
    lsl = db.Column(db.Float, nullable=False)
    measure_amount = db.Column(db.Float, nullable=False)
    range_spec = db.Column(db.Float, nullable=False)
    sample_number = db.Column(db.Float, nullable=False)
    rules = db.Column(
        db.String(64), nullable=False)

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
class spc_measure_point_history(db.Model): #Sojourn 2
    __tablename__='spc_measure_point_history'
    uuid = db.Column(
        db.String(30),unique = True,  primary_key = True, nullable = False)
    work_order_op_history_uuid = db.Column(
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
    value = db.Column(db.Float, nullable=False) #float?
    measure_object_id = db.Column(db.Float, nullable=False)
    spc_measure_instrument_uuid = db.Column(
        db.String(50), unique=False, nullable=False)
    
    def __init__(self,uuid,work_order_op_history_uuid,tenant_id,create_time,update_time,worker_id,spc_measure_point_config_uuid,value,measure_object_id,spc_measure_instrument_uuid):
        self.uuid = uuid
        self.work_order_op_history_uuid = work_order_op_history_uuid
        self.tenant_id = tenant_id
        self.create_time = create_time
        self.update_time = update_time
        self.worker_id = worker_id
        self.spc_measure_point_config_uuid = spc_measure_point_config_uuid
        self.value = value
        self.measure_object_id = measure_object_id
        self.spc_measure_instrument_uuid = spc_measure_instrument_uuid
        # self.state
class work_order_op_history(db.Model): #Sojourn 3
    __tablename__='work_order_op_history'
    uuid = db.Column(
        db.String(30),unique = True,  primary_key = True, nullable = False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)
    work_order_id = db.Column(
        db.String(30), unique=False, nullable=False)
    shift = db.Column(db.Float, nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.now)
    end_time = db.Column(
        db.DateTime, onupdate=datetime.now, default=datetime.now)
    producer_number = db.Column(
        db.String(50), unique=False, nullable=False)
    producer_name = db.Column(
        db.String(50), unique=False, nullable=False)
    qty = db.Column(db.Float, nullable=False)
    description = db.Column(
        db.String(255), nullable=False)
    device_name = db.Column(
        db.String(50), unique=False, nullable=False)
    good = db.Column(db.Float, nullable=False)
    defect = db.Column(db.Float, nullable=False)
    std_tp = db.Column(db.Float, nullable=False)
    std_ts = db.Column(db.Float, nullable=False)

    worker_uuid = db.Column(
        db.String(30), unique=False, nullable=False)
    work_order_uuid = db.Column(
        db.String(30), unique=False, nullable=False)
    operation_uuid = db.Column(
        db.String(30), unique=False, nullable=False)
    def __init__(self,uuid,create_time,update_time,work_order_id,start_time,end_time,producer_number,producer_name,qty,description,device_name,good,defect,std_tp,std_ts,std_work_time,operation_uuid):
        self.uuid = uuid
        self.create_time = create_time
        self.update_time = update_time
        self.work_order_id = work_order_id
        self.shift = shift
        self.start_time = start_time
        self.end_time = end_time
        self.producer_number = producer_number
        self.producer_name = producer_name
        self.qty = qty
        self.description = description
        self.device_name = device_name
        self.good = good
        self.defect = defect
        self.std_tp = std_tp
        self.std_ts = std_ts
        self.std_work_time = std_work_time
        self.worker_uuid = worker_uuid
        self.work_order_uuid = work_order_uuid
        self.operation_uuid = operation_uuid


class spcTable:
  def __init__(self):
    self.firstvar = begin_time
    self.lastvar = expiry_time

  def queryfunc(begin_time,expiry_time): # start_time,end_time,work_order_op_history_uuid,spc_measure_point_config_uuid
    # aliazed the table
    table_config = aliased(spc_measure_point_config) # operation_uuid <=> table_work_order
    table_history = aliased(spc_measure_point_history) # work_order_op_history_uuid <=> table_work_order.uuid
    table_work_order = aliased(work_order_op_history) # operation_uuid <=> table_config
    
    
    # stmt = select(spc_measure_point_history.work_order_op_history_uuid).where(spc_measure_point_history.spc_measure_point_config_uuid == '57016b97-2355-460f-b673-6512d8ed00da')
    Q_spchistory = select(table_history.uuid,table_history.value).where(table_history.uuid == '3aa29f18-4fc0-48d7-ab29-541d79c7998d')
    Q_spcconfig = select(table_config.uuid).where(table_config.uuid == '3aa29f18-4fc0-48d7-ab29-541d79c7998d')
    Q_work_order_op = select(table_work_order.start_time,table_work_order.end_time).where(table_work_order.uuid == '4b911c4c-9640-48c7-a99e-a09f9cfdb976')
    Q_result = select(table_config.uuid).where(table_config.uuid == '3aa29f18-4fc0-48d7-ab29-541d79c7998d')#.join_from()
    # table_history.value,table_work_order.good,table_work_order.defect,table_config.usl,table_config.lsl
    

    try:
        j1 = session.query(table_history.value,table_work_order.good,table_work_order.defect,table_config.lsl,table_config.usl)\
        .join(table_config, table_history.spc_measure_point_config_uuid == table_config.uuid)\
        .join(table_work_order, table_work_order.uuid == table_history.work_order_op_history_uuid)\
        .where((table_work_order.start_time > begin_time) & (table_work_order.end_time < expiry_time))
        # while (table_history.work_order_op_history_uuid and table_history.spc_measure_point_config_uuid)
        queryResult = [row for row in session.execute(j1)] #first() meant head

        valuelst = [item[0] for item in queryResult]
        goodlst = [item[1] for item in queryResult]
        defectlst = [item[2] for item in queryResult]
        lslspec = [item[3] for item in queryResult][0]
        uslspec = [item[4] for item in queryResult][0]
        # print(j1)
        # print("print: ", queryResult ,sep='\n')
        qResult = {"valuelst":valuelst,"goodlst":goodlst ,"defectlst":defectlst ,"lslspec": lslspec,"uslspec": uslspec}
        # consum fun from calculator 
        # 
        return qResult
        

    except Exception as e:
        print("error type: ",type(e),str(e))
        raise
  
    # print("jj", j1)
    # stmt = select(table_history).select_from(j1) #subquery
    # print("stmt:", stmt)
    # print(stmt)

    # QQ = session.query(table_history.value,table_config).join(table_history, table_history.spc_measure_point_config_uuid == table_config.uuid).filter(table_history.spc_measure_point_config_uuid == '57016b97-2355-460f-b673-6512d8ed00da')
    # print(QQ)
    # sql轉譯
    def printvar():
        print(self.firstvar, self.lastvar)


# print(spcTable.queryfunc())