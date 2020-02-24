from neuron import h, gui
from matplotlib import pyplot as plt
import numpy as np


def measure_width(trace):
    trace = np.array(trace)

    points = np.where(trace > (trace[15000] + 2))[0]
    points = points[np.logical_and(points >= 20000, points <= 30000)]

    width = dt * (points[-1] - points[0])

    return width

h.load_file('init_models_with_ca/init_model2.hoc')

locations = [0, 0.1, 0.3, 0.5, 0.7, 0.9, 1]
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

lengths = np.array([200, 300, 400, 500, 600])

fig, axes = plt.subplots(1, 2, sharex='all', squeeze=False, figsize=(16, 8))

for i in range(lengths.size):
    h.apical.L = lengths[i]

    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    h('recalculate_geometry()')

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

    maxV = [0] * len(probes)
    w = [0] * len(probes)

    for j in range(len(probes)):
        maxV[j] = np.max(np.array(probes[j]))
        w[j] = measure_width(probes[j])

    absolute_locations = np.array(locations) * lengths[i]
    axes[0, 0].plot(absolute_locations, maxV)
    axes[0, 1].plot(absolute_locations, w)

axes[0, 0].legend(lengths)

axes[0, 0].set_xlabel('distance from soma ($\u03BC$m)')
axes[0, 0].set_ylabel('peak voltage (mV)')
axes[0, 1].set_xlabel('distance from soma ($\u03BC$m)')
axes[0, 1].set_ylabel('width (ms)')
axes[0, 0].set_ylim(-70, 60)
axes[0, 1].set_ylim(0, 50)

plt.show()