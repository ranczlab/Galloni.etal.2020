from neuron import h
from matplotlib import pyplot as plt
import numpy as np


def set_default_length():
    h.apical.L = 600
    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    h('recalculate_geometry()')

    h.tuft.gbar_sca = 0

    return ()

h.load_file('init_models_with_ca/init_model2.hoc')
h.delete_section(sec=h.axon)
h.delete_section(sec=h.iseg)
h.delete_section(sec=h.hillock)

# Set up stimulus
default_amp = -40
default_dur = 10
stim = h.SEClamp(h.apical(1))
stim.amp1 = -70
stim.amp2 = default_amp
stim.amp3 = -70
stim.dur1 = 500
stim.dur2 = default_dur
stim.dur3 = 100

# Set up recording vectors
tuft_v_vec = h.Vector()
tuft_v_vec.record(h.tuft(.5)._ref_v)
t_vec = h.Vector()
t_vec.record(h._ref_t)

# Simulation parameters
dt = 0.025
h.tstop = 1000 - dt

h.tuft.gbar_sca = 0

durations = np.arange(0, 55, 5)
cm = np.linspace(1, 2.5, 5)
cm = np.around(cm, 1)

fig, axes = plt.subplots(1, 1, squeeze=False, sharex='all', sharey='row', figsize=(8, 8))

set_default_length()

maxV = np.zeros([durations.size, cm.size])

for i in range(durations.size):

    stim.dur2 = durations[i]
    stim.amp2 = default_amp

    for j in range(cm.size):
        h.tuft.cm = cm[j]

        h.run()

        maxV[i, j] = np.max(np.array(tuft_v_vec))

for k in range(cm.size):
    axes[0, 0].plot(durations, maxV[:, k])

axes[0, 0].set_xlabel('width (ms)')
axes[0, 0].set_ylabel('peak voltage (mV)')
axes[0, 0].legend(cm)
plt.show()