from neuron import h
from os import path
import argparse
import csv
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('LVA_volume', metavar = 'LVA', type=str)
args = parser.parse_args()

h.load_file('simulationcode/BAC_firing_long.hoc')

h.st1.amp = 1.9
h.syn1.imax = 0.5

h.run()

tvec = np.asarray(h.tvec)
vtuft = np.asarray(h.vdend2)
lower = 75
upper = -25

integral = np.trapz(((vtuft[lower:upper] - vtuft[75])/10**6), tvec[lower:upper])

fields = [args.LVA_volume, integral]
if path.exists('outputs/data/figure_3_supplementary_2d_long.csv'):
    with open(r'outputs/data/figure_3_supplementary_2d_long.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
else:
    with open(r'outputs/data/figure_3_supplementary_2d_long.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['LVA_volume', 'integral'])
        writer.writerow(fields)