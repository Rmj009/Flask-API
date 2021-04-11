# main.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
# from db-migrator import db
db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user_name:docusr@IP:5432/db-migrator"
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


@app.route('/')
def index():
    db.create_all()
    
    # Add data
    testxxx = spc_measure_point_history('Max',8888,'', '', '','')
    db.session.add(testxxx)
    db.session.commit()

    # Read data
    # query = spc_measure_point_history.query.filter_by(value = 12).first()
    # print(query.value)
    # print(query.uuid)

    # sql_cmd =
    #     SELECT *
    #     FROM spc_measure_point_history

    query_data = db.engine.execute(sql_cmd)
    print(query_data)
    return 'ok'

    # SELECT spc_measure_point_config.name, spc_measure_point_history.value,(spc_measure_point_config.usl+spc_measure_point_config.std_value) AS USL, (spc_measure_point_config.std_value-spc_measure_point_config.lsl) AS LSL --,spc_measure_point_history.measure_object_id

    # FROM spc_measure_point_config  left OUTER JOIN spc_measure_point_history
    # ON spc_measure_point_config.uuid = spc_measure_point_history.spc_measure_point_config_uuid

    # WHERE spc_measure_point_history.value NOT IN (-88888888)

    # order by spc_measure_point_config.uuid
    
    

