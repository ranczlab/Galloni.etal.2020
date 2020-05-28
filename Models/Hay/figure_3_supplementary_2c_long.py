import csv
import argparse
import numpy as np
from neuron import h
from os import path
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('hotspot_size', metavar = 'hotspot', type=int)
args = parser.parse_args()

h.load_file('simulationcode/BAC_firing_long.hoc')

h.st1.amp = 1.9
h.syn1.imax = 0.5
h.run()

tvec = np.array(h.tvec)
vsoma = np.array(h.vsoma)
vtuft = np.array(h.vdend2)

lower = 75
upper = -25

integral = np.trapz(((vtuft[lower:upper] - vtuft[75])/10**6), tvec[lower:upper])

fields = [args.hotspot_size, integral]
if path.exists('outputs/data/figure_3_supplementary_2c_long.csv'):
    with open(r'outputs/data/figure_3_supplementary_2c_long.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
else:
    with open(r'outputs/data/figure_3_supplementary_2c_long.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['hotspot_size', 'integral'])
        writer.writerow(fields)
