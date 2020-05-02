import csv
import matplotlib.pyplot as plt
import numpy as np 

short_gca = []
short_integral = []
with open('outputs/data/figure_3b_short.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        short_gca.append(row[0])
        short_integral.append(row[1])
        
short_hotspot_size = np.asarray([float(i) for i in short_hotspot_size])
short_integral = np.asarray([float(i) for i in short_integral])

long_gca = []
long_integral = []
with open('outputs/data/figure_3b_long.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        long_gca.append(row[0])
        long_integral.append(row[1])
        
long_gca = np.asarray([float(i) for i in long_gca])
long_integral = np.asarray([float(i) for i in long_integral])

plt.plot(short_gca, short_integral, 'k--')
plt.plot(long_gca, long_integral, 'k-')
plt.ylabel('Integral')
plt.xlabel('Hotspot size')
plt.ylim(0, 0.006)
plt.xlim(0, 8)

plt.savefig('outputs/figures/figure_3b_summary.svg')