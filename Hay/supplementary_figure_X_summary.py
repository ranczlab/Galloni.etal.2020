import csv
import matplotlib.pyplot as plt
import numpy as np 

isyn = []
voltage = []
baseline = []
with open('outputs/data/supplementary_figure_X_short.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        isyn.append(row[0])
        baseline.append(row[1])
        voltage.append(row[2])
        
isyn = np.asarray([float(i) for i in isyn])
baseline = np.asarray([float(i) for i in baseline])
voltage = np.asarray([float(i) for i in voltage])

longbaseline = []
longvoltage = []
with open('outputs/data/supplementary_figure_X_long.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        longbaseline.append(row[1])
        longvoltage.append(row[2])

longbaseline = np.asarray([float(i) for i in longbaseline])
longvoltage = np.asarray([float(i) for i in longvoltage])
longdepol = longvoltage - longbaseline
        
plt.figure(figsize=(16,16))
plt.plot(isyn, voltage, 'k-')
plt.axhline(longvoltage, color = 'black', ls = '--')
plt.ylabel('Maximum amplitude (mV)')
plt.xlabel('EPSP maxmimum amplitude (nA)')
plt.savefig('outputs/figures/supplementary_figure_X_amplitude.jpg')

plt.figure(figsize=(16,16))
depol = voltage - baseline
plt.plot(isyn, depol, 'k-')
plt.axhline(longdepol, color = 'black', ls = '--')
plt.ylabel('Maximum depolarization (mV)')
plt.xlabel('EPSP maxmimum amplitude (nA)')
plt.savefig('outputs/figures/supplementary_figure_X_depolarization.jpg')

