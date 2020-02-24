from neuron import h
from matplotlib import pyplot as plt
import numpy as np


def measure_width(trace):
    trace = np.array(trace)

    points = np.where(trace > (trace[15000] + 2))[0]
    points = points[np.logical_and(points >= 20000, points <= 30000)]

    width = dt * (points[-1] - points[0])

    return (width)


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

l = np.array([200, 300, 400, 500, 600])
fig, axes = plt.subplots(3, l.size, sharey='row', sharex='all', squeeze=False, figsize=(16, 16 / 4))

for i in range(l.size):
    h.apical.L = l[i]

    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    h('recalculate_geometry()')

    h.tuft.gbar_sca = 0

    h.run()

    axes[0, i].plot(t_vec, tuft_v_vec, color='red')
    axes[1, i].plot(t_vec, apical_end_v_vec, color='lightblue')
    axes[2, i].plot(t_vec, stim_vec, color='black')

    h.tuft.gbar_sca = default_sca

    h.run()

    axes[0, i].plot(t_vec, tuft_v_vec, color='red', linestyle='--')
    axes[1, i].plot(t_vec, apical_end_v_vec, color='lightblue', linestyle='--')

axes[0, 0].set_xlim(450, 650)
axes[0, 0].set_ylim(-80, 60)
axes[1, 0].set_ylim(-80, 60)
axes[2, 0].set_ylim(-1, 8)

plt.show()