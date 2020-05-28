import csv
import matplotlib.pyplot as plt
import numpy as np 

shortdata = []
with open('outputs/data/figure_3_supplementary_2f_short.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        shortdata.append(row[0])

longdata = []
with open('outputs/data/figure_3_supplementary_2f_long.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        longdata.append(row[0])

multipliers = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])

shortdata = [float(i) for i in shortdata]
longdata = [float(i) for i in longdata]

plt.plot(multipliers, shortdata, 'k--')
plt.plot(multipliers, longdata, 'k-')
plt.xlim(40, 210)
plt.savefig('outputs/figures/figure_3_supplementary_2f.svg')