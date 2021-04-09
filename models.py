import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import os

# class dashboard:
#     def isValidpoint(self): # the invoker is an object
#         p0 = 0.01 # where p is the probability that any point exceeds the control limits

#         if((0 <= self.alpha <= 1) and (0 <= self.beta <= 1)): #type I error acceptance
#             alpha.float = 0.05 ; ARL = 1/(1-p0)
#         return False
#     def caculator(self):
#         table[i][j] = [ enumerate(i,j) for i in lstRow for j in lstColumn] # enumerate all subgroup data
#         #self.mean = np.mean(i for i range len()); xbar = summarize overall / len(all data) #calculate subgroup mean/ total mean
#         # self.stdv = for subgroupData individual stdv ; overall stdv
#         # target UCL= ; target LCL; target Range
#     def TrivialPlot():
#         # a, b = np.polyfit(x, y, deg=1) # invoke Data, pd.dataFrame
#         # y_est = a * x + b # linear function; 
#         #-------------Time series figure //axis x; axis y 
#         # fig, ax = plt.subplots()
#         # ax.plot(x, y_est, '-')
#         # ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
#         # ax.plot(x, y, 'o', color='tab:brown')

#         # y_err = x.std() * np.sqrt(1/len(x) + (x - x.mean())**2 / np.sum((x - x.mean())**2)) # append auxiliary line
