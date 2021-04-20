import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat
from spcTable import *

data_transforms = None

# def load_data(cls_file, log_file):
#     global classes, megadata
#     # df = pd.read_json(r'file')
#     # djson = df.to_csv()
#     with open(cls_file, "r") as f:
#         djson = json.load(json_file)
#         # classes = f.read().split("\n")
#     with open(log_file, "r") as f:
#         megadata = f.read().split("\n")

def calc(mylst,usl,lsl,num_good,num_defect):
    ANS = 0,0,0,0 # return ans once exception occur
    try:
        arr = np.array(mylst)
        # print("arr: ",arr)
        arr = arr.ravel()
        # print("ravel, " ,arr)
        total_num = num_good + num_defect
        g_rate = good
        ngroup = 10 #input() #給使用者指定每組大小
        ppkarr = np.array_split(arr,ngroup)# 將資料分組計算
        ppkarrSig = [np.mean(i) for i in ppkarr]
        sigmaPpk = np.std(ppkarrSig)
        # print("sigmaPpk: ",sigmaPpk)
        sigmaCpk = np.std(arr)
        m = np.mean(arr) #median
        Cp = float(usl - lsl) / (6*sigmaCpk)
        Cpu = float(usl - m) / (3*sigmaCpk)
        Cpl = float(m - lsl) / (3*sigmaCpk)
        Cpk = np.min([Cpu, Cpl])
        ppu = float(usl - m) / (3*sigmaPpk)
        ppl = float(m - lsl) / (3*sigmaPpk)
        Ppk = np.min([ppu,ppl])
        ANS = total_num, Cp, Cpu, Cpk, Ppk
        return ANS #Cp, Cpu, Cpk, Ppk
    except  ZeroDivisionError() as e: # work on python 2.x
        print('sigma zero result from variance: '+ str(e))
        print("fix infinity")

def testRule1(obj,newNum, mean, sd):

    sigUp = mean + sd*3
    sigDown = mean - sd*3
    code = (newNum > sigUp) or (newNum < sigDown)
    obj['format_1'] = np.append(obj['format_1'],code)
    return

def testRule2(obj, newNum, mean, sd):
    twoSigUp = mean + sd*2
    twoSigDown = mean - sd*2
    temp_clipped = obj['all_vals'][-2:]
    temp_clipped = np.append(temp_clipped,newNum)
    above2 = temp_clipped > twoSigUp
    below2 = temp_clipped < twoSigDown
    code = (above2.sum(axis=0) >= 2) or (below2.sum(axis=0) >= 2)
    obj['format_2'] = np.append(obj['format_2'],code)
    return

def testRule3(obj, newNum, mean, sd):
    oneSigUp = mean + sd
    oneSigDown = mean - sd
    temp_clipped = obj['all_vals'][-5:]
    temp_clipped = np.append(temp_clipped,newNum)
    above1 = temp_clipped > oneSigUp
    below1 = temp_clipped < oneSigDown
    code = (above1.sum(axis=0) >= 4) or (below1.sum(axis=0) >= 4)
    obj['format_3'] = np.append(obj['format_3'],code)
    return
    
def testRule4(obj, newNum, mean):
    temp_clipped = obj['all_vals'][-8:]
    temp_clipped = np.append(temp_clipped,newNum)
    above = temp_clipped > mean
    below = temp_clipped < mean
    code = (above.sum(axis=0) >= 9) or (below.sum(axis=0) >= 9)
    obj['format_4'] = np.append(obj['format_4'],code)
    return

#Return the value's index if rule has been violated.  This is used for formatting.

def violations(obj,datum):
    theMean = np.mean(obj['all_vals'])
    sd = np.std(obj['all_vals'])
    testRule1(obj,datum, theMean, sd)
    testRule2(obj,datum, theMean, sd)
    testRule3(obj,datum, theMean, sd)
    testRule4(obj,datum, theMean)
    return
    
def assign_datum(obj,datum = None):
    if(datum is None):
        datum = rando()
    violations(obj,datum)
    obj['all_vals'] = np.append(obj['all_vals'],datum)
    return


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

# df=pd.read_csv('workbook_name.csv', sep=',',header=0); nmp = df.to_numpy()
 #nmp[:,11]

# def plotQuery():
# ptV = queryfunc()
# trendObj = {
# 'all_vals': ptV,
# 'format_1': np.zeros(len(ptV)),
# 'format_2': np.zeros(len(ptV)),
# 'format_3': np.zeros(len(ptV)),
# 'format_4': np.zeros(len(ptV))}

# plt.plot(trendObj['all_vals'])
# mark = 10.0
# plt.figure(figsize=(10,5))
# plt.plot(trendObj['all_vals'], color='red',markevery=format_arr(1), ls="", marker='x',mfc = 'none', mec='red', label="Rule1", markersize=mark*0.5)
# plt.plot(trendObj['all_vals'], color='blue',markevery=format_arr(2), ls="", marker='o', mfc='none',mec='blue',label="Rule2", markersize=mark*1)
# plt.plot(trendObj['all_vals'], color='brown',markevery=format_arr(3), ls="", marker='p', mfc='none',mec='brown',label="Rule3", markersize=mark*1.5)
# plt.plot(trendObj['all_vals'], color='blue',markevery=format_arr(4), ls="", marker='s', mfc='none',mec='green',label="Rule4", markersize=mark*1.0)
# plt.plot(trendObj['all_vals'], color='#81B5CB', ls="", marker="o", markersize=mark)
# plotAxlines(trendObj['all_vals'])
# plt.legend()
# plt.ylim(0,0.003)
# # plt.plot(ptV)
# plt.savefig('static/control-chart.png')
# # return plt.show()

# # plotQuery()