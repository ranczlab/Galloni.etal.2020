import argparse
import csv
import numpy as np
from os import path
from neuron import h
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('tuft_gca_multiplier', metavar = 'gCA', type=str)
args = parser.parse_args()

h.load_file('simulationcode/BAC_firing_short.hoc')

fig, axes = plt.subplots(2, 3, squeeze=False, sharex='all', sharey='row', figsize=(16, 8))

h.st1.dur = 3
h.st1.amp = 1.8
h.syn1.imax = 0.5

h.run()

tvec = np.asarray(h.tvec)
vtuft = np.asarray(h.vdend2)
lower = 75
upper = -25

integral = np.trapz(((vtuft[lower:upper] - vtuft[75])/10**6), tvec[lower:upper])

fields = [args.tuft_gca_multiplier, integral]
if path.exists('outputs/data/figure_3_supplementary_1d_short.csv'):
    with open(r'outputs/data/figure_3_supplementary_1d_short.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
else:
    with open(r'outputs/data/figure_3_supplementary_1d_short.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['gca_multiplier', 'integral'])
        writer.writerow(fields)
        

