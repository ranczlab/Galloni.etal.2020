from neuron import h, gui
from matplotlib import pyplot as plt
import numpy as np

h.load_file('init_models_with_ca/init_model2.hoc')

locations = [0, 0.3, 0.7, 1]
probes = [0] * len(locations)

# Set up stimulus
stim = h.Ipulse2(h.soma(.5))
stim.amp = 2
stim.dur = 3
stim.delay = 500
stim.per = 10
stim.num = 1

# Set up recording vectors
for i in range(len(probes)):
    probes[i] = h.Vector()
    probes[i].record(h.apical(locations[i])._ref_v)
t_vec = h.Vector()
t_vec.record(h._ref_t)

dt = 0.025
h.tstop = 1000 - dt

h.apical.L = 600

h('recalculate_passive_properties()')
h('recalculate_channel_densities()')
h('recalculate_geometry()')

h.tuft.gbar_sca = 0

fig, axes = plt.subplots(2, len(probes), sharex='all', sharey='all', squeeze=False, figsize=(16,2))

h.run()

for i in range(len(probes)):
    axes[0, i].plot(t_vec, probes[i])
    axes[0, i].set_title(locations[i] * h.apical.L)

h.apical.gbar_nat = 0
h.apical.gbar_kfast = 0
h.apical.gbar_kslow = 0
h.apical.gbar_ih = 0

h.tuft.gbar_sca = 0
h.tuft.gbar_nat = 0
h.tuft.gbar_kfast = 0
h.tuft.gbar_kslow = 0
h.tuft.gbar_ih = 0

h.run()

for i in range(len(probes)):
    axes[1, i].plot(t_vec, probes[i])

axes[0, 0].set_xlim(450, 650)
axes[0, 0].set_ylim(-100, 50)

plt.show()


