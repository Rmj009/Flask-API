import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import os


# n = [eval(i) for i in input()]
# a=[float(eval(i)) for i in input().split()]
os.system('export DISPLAY=:0.0')
x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]
N=21
# fit a linear curve an estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) + (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')

plt.plot(x,y)

#  {
#         "UUID": "35d804be-7c7f-4b1b-a8ee-51a13f6baab5",
#         "updateTime": "2021-03-17T05:27:21.551969Z",
#         "createTime": "2020-12-07T03:39:07.175088Z",
#         "tenantID": "group1-t0yq0",
#         "workOrderOpHistoryUUID": "4134d124-ddb0-4ef4-91ba-922710ec7d65",
#         "spcMeasurePointConfigUUID": "7202a1e7-346d-11eb-8118-3ee8fbec59ed",
#         "spcMeasureInstrumentUUID": "18689442-771b-11eb-9529-3262474ceeb7",
#         "measureObjectID": 1,
#         "workerID": "00001",
#         "value": 14,
#         "workOrderOpHistory": {
#             "UUID": "4134d124-ddb0-4ef4-91ba-922710ec7d65",
#             "updateTime": "2020-06-05T04:07:18Z",
#             "createTime": "2020-06-05T03:46:27Z",
#             "tenantID": "group1-t0yq0",
#             "workOrderID": "21067983",
#             "shift": "",
#             "startTime": "2020-06-05T03:54:13Z",
#             "endTime": "2020-06-05T04:07:18Z",
#             "productNumber": "534-02-004",
#             "productName": "Z軸馬達托架(ME類)",
#             "qty": 50,
#             "description": "工程一(銑四周面及柱坑各孔)",
#             "deviceName": "MC-44",
#             "good": 50,
#             "defect": 0,
#             "stdTp": 50,
#             "stdTs": 80,
#             "stdWorkTime": 4050,
#             "actWorkTime": 785.985564279,
#             "workerID": "00273",
#             "workerName": "吳昇霖",
#             "progress": 0,
#             "defectReason": "",
#             "opCode": "20",
#             "workerUUID": "fb749eac-9459-4a25-ba83-2ab859a3ef77",
#             "workOrderUUID": "6d6567d8-a756-46ad-89c1-3e1140f7340a",
#             "operationUUID": "97a1f322-1ed5-40d0-b933-11cd687e5ff7",
#             "deviceUUID": "97fedfea-46c2-4b8d-a821-6cba3906b657",
#             "status": 3,
#             "opOrder": 1,
#             "deviceType": 0,
#             "abnormalStatus": null,
#             "opName": "20",
#             "estimatedTime": "0001-01-01T00:00:00Z"
#         },
#         "spcMeasureInstrument": {
#             "UUID": "18689442-771b-11eb-9529-3262474ceeb7",
#             "updateTime": "2021-02-25T03:39:42.226132Z",
#             "createTime": "2021-02-25T03:39:42.226132Z",
#             "tenantID": "group1-t0yq0",
#             "name": "游標卡尺",
#             "description": "游標卡尺"
#         }
#     },