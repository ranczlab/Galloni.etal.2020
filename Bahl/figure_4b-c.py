from neuron import h
from matplotlib import pyplot as plt
import numpy as np


def measure_width(trace):
    trace = np.array(trace)

    points = np.where(trace > (trace[15000] + 2))[0]
    points = points[np.logical_and(points >= 20000, points <= 30000)]

    width = dt * (points[-1] - points[0])

    return width


h.load_file('init_models_with_ca/init_model2.hoc')
default_sca = h.tuft.gbar_sca

# Set up stimulus
stim = h.Ipulse2(h.soma(.5))
stim.amp = 2
stim.dur = 3
stim.delay = 500
stim.per = 10
stim.num = 3

# Set up recording vectors
soma_v_vec = h.Vector()
soma_v_vec.record(h.soma(.5)._ref_v)
apical_end_v_vec = h.Vector()
apical_end_v_vec.record(h.apical(1)._ref_v)
tuft_v_vec = h.Vector()
tuft_v_vec.record(h.tuft(.5)._ref_v)
stim_vec = h.Vector()
stim_vec.record(stim._ref_i)
t_vec = h.Vector()
t_vec.record(h._ref_t)

# Simulation parameters
dt = 0.025
h.tstop = 1000 - dt

l = np.arange(200, 650, 50)
fig, axes = plt.subplots(1, 2, sharex='all', squeeze=False, figsize=(32, 15))

maxV = np.zeros([4, l.size])
w = np.zeros([4, l.size])

for i in range(l.size):
    h.apical.L = l[i]

    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    h('recalculate_geometry()')

    h.tuft.gbar_sca = 0

    h.run()

    maxV[0, i] = np.max(np.array(apical_end_v_vec))
    maxV[1, i] = np.max(np.array(tuft_v_vec))

    w[0, i] = measure_width(apical_end_v_vec)
    w[1, i] = measure_width(tuft_v_vec)

    h.tuft.gbar_sca = default_sca

    h.run()

    maxV[2, i] = np.max(np.array(apical_end_v_vec))
    maxV[3, i] = np.max(np.array(tuft_v_vec))

    w[2, i] = measure_width(apical_end_v_vec)
    w[3, i] = measure_width(tuft_v_vec)

axes[0, 0].plot(l, maxV[0, ], color='blue')
axes[0, 0].plot(l, maxV[2, ], color='blue', linestyle='--')
axes[0, 0].plot(l, maxV[1, ], color='red')
axes[0, 0].plot(l, maxV[3, ], color='red', linestyle='--')

axes[0, 1].plot(l, w[0, ], color='blue')
axes[0, 1].plot(l, w[2, ], color='blue', linestyle='--')
axes[0, 1].plot(l, w[1, ], color='red')
axes[0, 1].plot(l, w[3, ], color='red', linestyle='--')

axes[0, 0].set_xlabel('length (um)')
axes[0, 0].set_ylabel('peak voltage (mV)')

axes[0, 1].set_xlabel('length (um)')
axes[0, 1].set_ylabel('width (ms)')

axes[0, 0].set_ylim(-80, 20)
axes[0, 1].set_ylim(0, 100)

plt.savefig('outputs/figures/figure_4b-c.svg')
