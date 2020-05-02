from neuron import h
from matplotlib import pyplot as plt
import numpy as np
from os import path
import csv

h.load_file('simulationcode/BAC_firing_short.hoc')

fig, axes = plt.subplots(2, 1, squeeze = False, sharex = 'all', sharey = 'row', figsize = (8, 8))

amps = np.arange(-0.4, 0.62, .02)
for i in range(amps.size):
    h.st1.amp = amps[i]
    h.st1.dur = 500
    h.syn1.imax = 0
    h.tstop = 1000

    h.run()

    axes[0,0].plot(h.tvec, h.vsoma)
    axes[1,0].plot(h.tvec, h.isoma)
    
    fields = np.array(h.vsoma)
    
    if path.exists('outputs/data/figure_2_supplementary_3b_short.csv'):
        with open(r'outputs/data/figure_2_supplementary_3b_short.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
    else:
        with open(r'outputs/data/figure_2_supplementary_3b_short.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
        
    fields = np.array(h.tvec)
    
    if path.exists('outputs/data/figure_2_supplementary_3b_short_time.csv'):
        with open(r'outputs/data/figure_2_supplementary_3b_short_time.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
    else:
        with open(r'outputs/data/figure_2_supplementary_3b_short_time.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)


plt.xlim(100, 1000)
axes[0,0].set_ylim(-150, 70)
plt.savefig('outputs/figures/figure_2_supplementary_3b_short.svg')

fields = amps

if path.exists('outputs/data/figure_2_supplementary_3b_short_inputs.csv'):
    with open(r'outputs/data/figure_2_supplementary_3b_short_inputs.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
else:
    with open(r'outputs/data/figure_2_supplementary_3b_short_inputs.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(fields)