import csv
import numpy as np
import argparse
from os import path
from neuron import h
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('tuft_gca_multiplier', metavar = 'gCA', type=str)
args = parser.parse_args()

h.load_file('simulationcode/BAC_firing_short.hoc')


h('''
objref tuftica
access L5PC.apic[siteVec[0]]
tuftica = new Vector()
cvode.record(&ica(siteVec[1]),tuftica,tvec)''')

h.st1.dur = 3
h.st1.amp = 1.8
h.syn1.imax = 0.218

h.run()

tvec = np.array(h.tvec)
icavec = np.array(h.tuftica)

plt.plot(tvec, icavec)
plt.xlabel('time (ms)')
plt.ylabel('Ca current (mA/cm2)')
plt.xlim(275, 400)
plt.ylim(0, -0.000005)
plt.savefig('outputs/figures/figure_3_supplementary_1b_short_gca%s.svg' % str(args.tuft_gca_multiplier))
        

        

