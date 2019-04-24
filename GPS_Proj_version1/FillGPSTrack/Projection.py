# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 12:29
# @Author  : WHS
# @File    : Projection.py
# @Software: PyCharm
from matplotlib import pyplot as plt
import numpy as np

file = open(r'C:\Users\WHS\Desktop\top200wFillRoad.txt','r')
arrayLines = file.readlines()
index = 0
fig = plt.figure()
axes = fig.add_subplot(111)

for line in arrayLines:
    if(index==0 or index==1):
        axes.scatter(line.split("  ")[-2], line.split("  ")[-1], color='red',marker='.')
    else:
        axes.scatter(line.split("  ")[-2], line.split("  ")[-1], color='black',marker='.')
    index += 1
#plt.xlim(115,118)
#plt.ylim(39,42)
#plt.xticks(np.linspace(115,118,10))
#plt.yticks(np.linspace(39,42,10))
plt.grid(True)
plt.xlabel('lon')
plt.ylabel('lat')
plt.title('Road')
plt.show()