import csv
import numpy as np
from neuron import h
from os import path

h.load_file('simulationcode/BAC_firing_short.hoc')
allisyn = np.arange(0.1, 0.502, 0.0001)

lower = 75
upper = 250

baselines = []
amplitudes = []

for j in range(allisyn.size):
    isyn = allisyn[j]

    h.st1.amp = 0
    h.syn1.imax = isyn
    
    h.run()
    
    tvec = np.asarray(h.tvec)
    vtuft = np.asarray(h.vdend2)
    
    baseline = vtuft[lower]
    amplitude = np.max(vtuft[lower:upper])
    
    fields = [isyn, baseline, amplitude]
    if path.exists('outputs/data/supplementary_figure_X_short.csv'):
        with open(r'outputs/data/supplementary_figure_X_short.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
    else:
        with open(r'outputs/data/supplementary_figure_X_short.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['isyn', 'baseline', 'amplitude'])
            writer.writerow(fields)
