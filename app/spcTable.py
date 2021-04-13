from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import text
db = SQLAlchemy()

"""
Definition of the table format
1. spc_measure_point_config
2. spc_measure_point_history
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
