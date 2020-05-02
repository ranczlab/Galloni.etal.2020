import numpy as np
from neuron import h
from matplotlib import pyplot as plt
from os import path
import csv 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('hotspot', metavar = 'hotspot', type=str)
args = parser.parse_args()

fig, axes = plt.subplots(4, sharex = 'row', sharey = 'row')

h.load_file('simulationcode/critical_frequency_short.hoc')


h('''
objref tuftica
access L5PC.apic[siteVec[0]]
tuftica = new Vector()
cvode.record(&ica(siteVec[1]),tuftica,vsoma_t)''')

h.run()

vsoma = np.array(h.vsoma)
tvec = np.array(h.vsoma_t)

baseline = (np.abs(tvec - 200)).argmin() # 200 ms
lower = (np.abs(tvec - 275)).argmin()
upper = (np.abs(tvec - 325)).argmin()

axes[0].plot(h.vsoma_t, h.vsoma)
axes[0].plot(h.vsoma_t, h.vdend)
axes[1].plot(h.vsoma_t, h.istim[0], 'k')
axes[1].plot(h.vsoma_t, h.istim[1], 'k')
axes[1].plot(h.vsoma_t, h.istim[2], 'k')
axes[2].plot(h.vsoma_t, h.tuftica)
axes[0].plot([tvec[baseline], tvec[lower], tvec[upper]], [vsoma[baseline], vsoma[lower], vsoma[upper]], 'x')

axes[3].plot(tvec[lower:upper], vsoma[lower:upper])

axes[0].set_xlim(200, 400)
axes[2].set_xlim(200, 400)
axes[1].set_xlim(200, 400)

plt.savefig('outputs/figures/traces/figure_3_supplementary_2e_short_%s.svg' % args.hotspot)
integral = np.trapz((vsoma[lower:upper] - vsoma[baseline])/10**6, tvec[lower:upper])

if path.exists('outputs/data/figure_3_supplementary_2f_short.csv'):
    with open(r'outputs/data/figure_3_supplementary_2f_short.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([integral])
else:
    with open(r'outputs/data/figure_3_supplementary_2f_short.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow([integral])