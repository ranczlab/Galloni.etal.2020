import csv
import matplotlib.pyplot as plt
import numpy as np 

shortdata = []
with open('outputs/data/figure_ratio_short.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        shortdata.append(row[1])

longdata = []
with open('outputs/data/figure_ratio_long.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        longdata.append(row[1])

LVA_volume = np.arange(0.001, 0.1, 0.009)

shortdata = [float(i) for i in shortdata]
longdata = [float(i) for i in longdata]

plt.plot(LVA_volume, shortdata, 'k--')
plt.plot(LVA_volume, longdata, 'k-')
plt.xscale('log')
plt.xticks([0.001, 0.01, 0.1], ['100:1', '10:1', '1:10'])
plt.ylim(0, 0.002)
plt.xlabel('HVA:LVA ratio')
plt.ylabel('Integral')
plt.savefig('outputs/figures/figure_ratio_summary.svg')