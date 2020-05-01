import csv
import numpy as np
from neuron import h
from os import path

h.load_file('simulationcode/BAC_firing_long.hoc')

lower = 75
upper = 250

h.st1.amp = 0
h.syn1.imax = 0.5
h.run()

tvec = np.asarray(h.tvec)
vtuft = np.asarray(h.vdend2)
    
baseline = vtuft[lower]
amplitude = np.max(vtuft[lower:upper])
    
fields = [0.5, baseline, amplitude]
with open(r'outputs/data/supplementary_figure_X_long.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['isyn', 'baseline', 'amplitude'])
    writer.writerow(fields)
        