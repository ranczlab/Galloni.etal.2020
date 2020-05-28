from matplotlib import pyplot as plt
from neuron import h

h.load_file('simulationcode/BAC_firing_short.hoc')

fig, axes = plt.subplots(2, 3, squeeze=False, sharex='all', sharey='row', figsize=(16, 8))

h.st1.dur = 3

h.st1.amp = 0
h.syn1.imax = 0.217

h.run()

axes[0,0].plot(h.tvec, h.vsoma, 'k')
axes[0,0].plot(h.tvec, h.vdend)
axes[0,0].plot(h.tvec, h.vdend2)
axes[0,0].set_ylim(-100, 60)

axes[1,0].plot(h.tvec, h.isoma, 'k')
axes[1,0].plot(h.tvec, -h.isyn, 'r')
axes[1,0].set_ylim(0,2)

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

h.st1.amp = 1.8
h.syn1.imax = 0.217

h.run()

axes[0,2].plot(h.tvec, h.vsoma, 'k')
axes[0,2].plot(h.tvec, h.vdend)
axes[0,2].plot(h.tvec, h.vdend2)
axes[0,2].set_ylim(-100, 60)

axes[1,2].plot(h.tvec, h.isoma, 'k')
axes[1,2].plot(h.tvec, -h.isyn, 'r')
axes[1,2].set_ylim(0,2)

plt.xlim(275, 400)
plt.savefig('outputs/figures/figure_3a_short.svg')