import csv
import argparse
import numpy as np
from neuron import h
from os import path
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('hotspot_size', metavar = 'hotspot', type=int)
args = parser.parse_args()

h.load_file('simulationcode/BAC_firing_short.hoc')

h.st1.amp = 1.8
h.st1.dur = 3
h.syn1.imax = 0.217
h.run()

tvec = np.array(h.tvec)
vsoma = np.array(h.vsoma)
vtuft = np.array(h.vdend2)

lower = 75
upper = -25

integral = np.trapz(((vtuft[lower:upper] - vtuft[75])/10**6), tvec[lower:upper])
v = vsoma
v[v < 0] = 0
v[v > 0] = 1
nspikes = np.sum(np.diff(v) > 0)

fields = [args.hotspot_size, nspikes, integral]
if path.exists('outputs/data/supplementary_figure_W_short.csv'):
    with open(r'outputs/data/supplementary_figure_W_short.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
else:
    with open(r'outputs/data/supplementary_figure_W_short.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['hotspot_size', 'nspikes', 'integral'])
        writer.writerow(fields)
