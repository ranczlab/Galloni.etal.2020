from matplotlib import pyplot as plt
from neuron import h

h.load_file('simulationcode/BAC_firing_short.hoc')

h('''
objref tuftica
access L5PC.apic[siteVec[0]]
tuftica = new Vector()
cvode.record(&ica(siteVec[1]),tuftica,tvec)''')

fig, axes = plt.subplots(3, 3, squeeze=False, sharex='all', sharey='row', figsize=(16, 8))

h.st1.dur = 3

h.st1.amp = 0
h.syn1.imax = 0.5

h.run()

axes[0,0].plot(h.tvec, h.vsoma, 'k')
axes[0,0].plot(h.tvec, h.vdend)
axes[0,0].plot(h.tvec, h.vdend2)
axes[0,0].set_ylim(-100, 60)

axes[1,0].plot(h.tvec, h.isoma, 'k')
axes[1,0].plot(h.tvec, -h.isyn, 'r')
axes[1,0].set_ylim(0,2)

axes[2,0].plot(h.tvec, h.tuftica)
axes[2,0].set_ylim(0, -0.006)

h.st1.amp = 1.8
h.syn1.imax = 0

h.run()

axes[0,1].plot(h.tvec, h.vsoma, 'k')
axes[0,1].plot(h.tvec, h.vdend)
axes[0,1].plot(h.tvec, h.vdend2)
axes[0,1].set_ylim(-100, 60)

axes[1,1].plot(h.tvec, h.isoma, 'k')
axes[1,1].plot(h.tvec, -h.isyn, 'r')
axes[1,1].set_ylim(0,2)

axes[2,1].plot(h.tvec, h.tuftica)
axes[2,1].set_ylim(0, -0.006)

h.st1.amp = 1.8
h.syn1.imax = 0.5

h.run()

axes[0,2].plot(h.tvec, h.vsoma, 'k')
axes[0,2].plot(h.tvec, h.vdend)
axes[0,2].plot(h.tvec, h.vdend2)
axes[0,2].set_ylim(-100, 60)

axes[1,2].plot(h.tvec, h.isoma, 'k')
axes[1,2].plot(h.tvec, -h.isyn, 'r')
axes[1,2].set_ylim(0,2)

axes[2,2].plot(h.tvec, h.tuftica)
axes[2,2].set_ylim(0, -0.006)

plt.xlim(275, 400)
plt.savefig('outputs/figures/figure_3_supplementary_1c.svg')