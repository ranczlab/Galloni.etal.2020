import csv
import matplotlib.pyplot as plt
import numpy as np 

shortdata = []
with open('outputs/data/figure_3_supplementary_1d_short.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        shortdata.append(row[1])

longdata = []
with open('outputs/data/figure_3_supplementary_1d_long.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        longdata.append(row[1])

multipliers = list(range(0,9))

shortdata = [float(i) for i in shortdata]
longdata = [float(i) for i in longdata]

plt.plot(multipliers, shortdata, 'k--')
plt.plot(multipliers, longdata, 'k-')
plt.savefig('outputs/figures/figure_3_supplementary_1d_summary.svg')