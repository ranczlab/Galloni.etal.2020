import csv
import matplotlib.pyplot as plt
import numpy as np 

short_hotspot_size = []
short_integral = []
with open('outputs/data/figure_3_supplementary_2c_short.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        short_hotspot_size.append(row[0])
        short_integral.append(row[1])
        
short_hotspot_size = np.asarray([float(i) for i in short_hotspot_size])
short_integral = np.asarray([float(i) for i in short_integral])

long_hotspot_size = []
long_integral = []
with open('outputs/data/figure_3_supplementary_2c_long.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        long_hotspot_size.append(row[0])
        long_integral.append(row[1])
        
long_hotspot_size = np.asarray([float(i) for i in long_hotspot_size])
long_integral = np.asarray([float(i) for i in long_integral])

plt.plot(short_hotspot_size, short_integral, 'k--')
plt.plot(long_hotspot_size, long_integral, 'k-')
plt.ylabel('Integral')
plt.xlabel('Hotspot size')
plt.ylim(0, 0.002)
plt.xlim(50, 200)

plt.savefig('outputs/figures/figure_3_supplementary_2c_summary.svg')