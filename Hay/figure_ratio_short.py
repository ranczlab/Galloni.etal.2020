from neuron import h
from matplotlib import pyplot as plt
import argparse
import csv
import numpy as np
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('LVA_volume', metavar = 'LVA', type=str)
args = parser.parse_args()

h.load_file('simulationcode/BAC_firing_short.hoc')

fig, axes = plt.subplots(2, 3, squeeze=False, sharex='all', sharey='row', figsize=(16, 8))

h.st1.amp = 1.8
h.syn1.imax = 0.217

h.run()

tvec = np.asarray(h.tvec)
vtuft = np.asarray(h.vdend2)
lower = 75
upper = -25

integral = np.trapz(((vtuft[lower:upper] - vtuft[75])/10**6), tvec[lower:upper])

fields = [args.LVA_volume, integral]
if path.exists('outputs/data/figure_ratio_short.csv'):
    with open(r'outputs/data/figure_ratio_short.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
else:
    with open(r'outputs/data/figure_ratio_short.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['LVA_volume', 'integral'])
        writer.writerow(fields)