from spcchart import SpcChart
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from spc import *
df = pd.read_csv('workbook_name.csv', sep=',',header=0)
data = df.to_numpy()
datalen = len(data[:,11])

result_spc = Spc(data[:,11], CHART_X_MR_MR)

result_spc.get_stats()
    # (2.875, 0.21542553191489322, 5.5345744680851068)
result_spc.get_violating_points()
    # {'1 beyond 3*sigma': [7]}
# result_spc.get_chart()
# s = Spc([1, 2, 3, 3, 2, 1, 3, 8], CHART_CUSUM)
# s.get_stats()
#     # (0, None, None)
# s.get_violating_points()
    # {'7 on one side': [7, 8], '1 beyond 3*sigma': [1, 2, 3, 4, 5, 6, 7, 8]}
print(result_spc)
print(type(data[:,11]))