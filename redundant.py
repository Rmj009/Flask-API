# app.py
## resultCapablity = dict(zip(keys, calc(mylst = queryfunc(mylst, usl=100, lsl=10,num_good= 111,num_defect= 222))) 
"""
map(dict, map(lambda t:zip(('num','char'),t), zip(list_nums,list_chars))) # [values for key,values in d.items()]
"""

# def load_data(cls_file, log_file):
#     global classes, megadata
#     # df = pd.read_json(r'file')
#     # djson = df.to_csv()
#     with open(cls_file, "r") as f:
#         djson = json.load(json_file)
#         # classes = f.read().split("\n")
#     with open(log_file, "r") as f:
#         megadata = f.read().split("\n")


# # method_a starts a transaction and calls method_b
    # def method_a(connection):
    #     with connection.begin():  # open a transaction
    #         method_b(connection)

    # # method_b also starts a transaction
    # def method_b(connection):
    #     with connection.begin(): # open a transaction - this runs in the context of method_a's transaction
    #         connection.execute(sql_cmd)
    # #-----------------------------------------------------------------
    # # # result = connection.execute(sql_cmd).first()[0]
    # result = db.engine.execute(text("sql_cmd").execution_options(autocommit=True))
    # # user = db.session.query().from_statement(text(sql_cmd)).params(name="").all()
    # Read data
    # #-----------------------------------------------------------------
    # resultproxy = engine.execute(sql_cmd)
    # response = [{column: vv for column, vv in row.items()} for row in resultproxy] # querydata transfer while fetch all item
    # # d, a = {}, []
    # # for row in resultproxy:
    # # # row.items() returns an array like [(key0, value0), (key1, value1)]
    # #     for column, value in row.items():
    # #     # build up the dictionary
    # #         d = {**d, **{column: value}}
    # #     a.append(d)
    
    # Qry = [item['value'] for item in response] # filter out all value in item
    # query = spc_measure_point_history.query.filter_by(spc_measure_point_config_uuid='57016b97-2355-460f-b673-6512d8ed00da').first()
    # prevent SQLQuery injection


# # stmt = select(spc_measure_point_history.work_order_op_history_uuid).where(spc_measure_point_history.spc_measure_point_config_uuid == '57016b97-2355-460f-b673-6512d8ed00da')
#     Q_spchistory = select(table_history.uuid,table_history.value).where(table_history.uuid == '3aa29f18-4fc0-48d7-ab29-541d79c7998d')
#     Q_spcconfig = select(table_config.uuid).where(table_config.uuid == '3aa29f18-4fc0-48d7-ab29-541d79c7998d')
#     Q_work_order_op = select(table_work_order.start_time,table_work_order.end_time).where(table_work_order.uuid == '4b911c4c-9640-48c7-a99e-a09f9cfdb976')
#     Q_result = select(table_config.uuid).where(table_config.uuid == '3aa29f18-4fc0-48d7-ab29-541d79c7998d')#.join_from()
#     # table_history.value,table_work_order.good,table_work_order.defect,table_config.usl,table_config.lsl



# sql_cmd = (
    #     """
    #     SELECT value, spc_measure_point_config_uuid FROM spc_measure_point_history
    #     WHERE value NOT IN (-88888888) and spc_measure_point_config_uuid='57016b97-2355-460f-b673-6512d8ed00da';

    #     """
    #     )
    # sql_cmd = (
    #     """
    #     select * 
    #     from spc_measure_point_config 
    #     where uuid = '57016b97-2355-460f-b673-6512d8ed00da'
    #     """
    # # )
    # sql_cmd = (
    #     """
    #     SELECT work_order_id 
    #     FROM work_order_op_history
    #     WHERE work_order_id == 11024776
    #     """
    # )