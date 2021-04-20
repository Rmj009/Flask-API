from flask import Flask, request, render_template, abort, url_for, json, jsonify, escape
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import text
from sqlalchemy.sql import text
from sqlalchemy import select
from calculator import *  #load_manuplate # ./../
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
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
    value = db.Column(db.Integer, nullable=False)
    measure_object_id = db.Column(db.Integer, nullable=False)
    spc_measure_instrument_uuid = db.Column(
        db.String(50), unique=False, nullable=False)
    # state = db.Column(
    #     db.String(30), unique=True, nullable=False)
    
    def __repr__(self,uuid,work_order_op_history_uuid,tenant_id,create_time,update_time,worker_id,spc_measure_point_config_uuid,value,measure_object_id,spc_measure_instrument_uuid):
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

# query = spc_measure_point_history.query.filter_by(spc_measure_point_config_uuid='57016b97-2355-460f-b673-6512d8ed00da').first()
# print(query)

stmt = select(spc_measure_point_history.work_order_op_history_uuid).where(spc_measure_point_history.spc_measure_point_config_uuid == '57016b97-2355-460f-b673-6512d8ed00da')
# QspcHistory = select(spc_measure_point_history.work_oder_op_history_uuid).where(spc_measure_point_history.spc_measure_point_config_uuid == '57016b97-2355-460f-b673-6512d8ed00da')
# sql轉譯
# print(result)

# for row in session.execute(stmt):
#         print(row)
#         count += 1
queryResult = [row for row in session.execute(stmt)]
print("stms: ", queryResult)

def qquery():
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
        SELECT value, spc_measure_point_config_uuid FROM spc_measure_point_history
        WHERE value NOT IN (-88888888) and spc_measure_point_config_uuid='57016b97-2355-460f-b673-6512d8ed00da';

        """
        )
    # sql_cmd = (
    #     """
    #     select * 
    #     from spc_measure_point_config 
    #     where uuid = '57016b97-2355-460f-b673-6512d8ed00da'
    #     """
    # )

    # method_a starts a transaction and calls method_b
    def method_a(connection):
        with connection.begin():  # open a transaction
            method_b(connection)

    # method_b also starts a transaction
    def method_b(connection):
        with connection.begin(): # open a transaction - this runs in the context of method_a's transaction
            connection.execute(sql_cmd)
    #-----------------------------------------------------------------
    # # result = connection.execute(sql_cmd).first()[0]
    # result = db.engine.execute(text("sql_cmd").execution_options(autocommit=True))
    # # user = db.session.query().from_statement(text(sql_cmd)).params(name="").all()
    # Read data
    
    # print(query)
    #-----------------------------------------------------------------
    resultproxy = engine.execute(sql_cmd)
    response = [{column: value for column, value in row.items()} for row in resultproxy] # querydata transfer while fetch all item
    # d, a = {}, []
    # for row in resultproxy:
    # # row.items() returns an array like [(key0, value0), (key1, value1)]
    #     for column, value in row.items():
    #     # build up the dictionary
    #         d = {**d, **{column: value}}
    #     a.append(d)
    Qry = [item['value'] for item in response] # fetch all value in item
    # print(Qry)
    
    return Qry #'ok', #,result