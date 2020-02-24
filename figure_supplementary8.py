from neuron import h
from matplotlib import pyplot as plt
import numpy as np


def measure_width(trace):
    trace = np.array(trace)

    points = np.where(trace > (trace[15000] + 2))[0]
    points = points[np.logical_and(points >= 20000, points <= 30000)]

    width = dt * (points[-1] - points[0])

    return width


def flatten_trunk_channels():
    gbar_nat = []
    gbar_ih = []
    gbar_kfast = []
    gbar_kslow = []

    for seg in h.apical:
        gbar_nat.append(seg.gbar_nat)
        gbar_ih.append(seg.gbar_ih)
        gbar_kfast.append(seg.gbar_kfast)
        gbar_kslow.append(seg.gbar_kslow)

    gbar_nat = (sum(gbar_nat) / 5)
    gbar_ih = (sum(gbar_ih) / 5)
    gbar_kfast = (sum(gbar_kfast) / 5)
    gbar_kslow = (sum(gbar_kslow) / 5)

    for seg in h.apical:
        seg.gbar_nat = gbar_nat
        seg.gbar_ih = gbar_ih
        seg.gbar_kfast = gbar_kfast
        seg.gbar_kslow = gbar_kslow

    return ()

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

dt = 0.025
h.tstop = 1000 - dt

l = np.arange(200, 650, 50)
fig, axes = plt.subplots(3, l.size, sharey='row', sharex='all', squeeze=False, figsize=(16, 16 / 4))

for i in range(l.size):
    h.apical.L = l[i]

    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    h('recalculate_geometry()')

    flatten_trunk_channels()

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

fig, axes = plt.subplots(1, 3, sharex=True, squeeze=False, figsize=(32, 15))

maxV = np.zeros([4, l.size])
w = np.zeros([4, l.size])
integral = np.zeros([4, l.size])

for i in range(l.size):
    h.apical.L = l[i]

    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    h('recalculate_geometry()')

    flatten_trunk_channels()

    h.tuft.gbar_sca = 0

    h.run()

    maxV[0, i] = np.max(np.array(apical_end_v_vec))
    maxV[1, i] = np.max(np.array(tuft_v_vec))

    w[0, i] = measure_width(apical_end_v_vec)
    w[1, i] = measure_width(tuft_v_vec)

    integral[0, i] = np.trapz(((np.array(apical_end_v_vec)[20000:25000] - apical_end_v_vec[15000]) / 10 ** 6), dx=0.025)
    integral[1, i] = np.trapz(((np.array(tuft_v_vec)[20000:25000] - tuft_v_vec[15000]) / 10 ** 6), dx=0.025)

    h.tuft.gbar_sca = default_sca

    h.run()

    maxV[2, i] = np.max(np.array(apical_end_v_vec))
    maxV[3, i] = np.max(np.array(tuft_v_vec))

    w[2, i] = measure_width(apical_end_v_vec)
    w[3, i] = measure_width(tuft_v_vec)

    integral[2, i] = np.trapz(((np.array(apical_end_v_vec)[20000:25000] - apical_end_v_vec[15000]) / 10 ** 6), dx=0.025)
    integral[3, i] = np.trapz(((np.array(tuft_v_vec)[20000:25000] - tuft_v_vec[15000]) / 10 ** 6), dx=0.025)

axes[0, 0].plot(l, maxV[0, ], color='blue')
axes[0, 0].plot(l, maxV[2, ], color='blue', linestyle='--')
axes[0, 0].plot(l, maxV[1, ], color='red')
axes[0, 0].plot(l, maxV[3, ], color='red', linestyle='--')

axes[0, 1].plot(l, w[0, ], color='blue')
axes[0, 1].plot(l, w[2, ], color='blue', linestyle='--')
axes[0, 1].plot(l, w[1, ], color='red')
axes[0, 1].plot(l, w[3, ], color='red', linestyle='--')

axes[0, 2].plot(l, integral[0, ], color='blue')
axes[0, 2].plot(l, integral[2, ], color='blue', linestyle='--')
axes[0, 2].plot(l, integral[1, ], color='red')
axes[0, 2].plot(l, integral[3, ], color='red', linestyle='--')

axes[0, 0].set_xlabel('length ($\u03BC$m)')
axes[0, 0].set_ylabel('peak voltage (mV)')

axes[0, 1].set_xlabel('length ($\u03BC$m)')
axes[0, 1].set_ylabel('width (ms)')

axes[0, 2].set_xlabel('length ($\u03BC$m)')
axes[0, 2].set_ylabel('integral (V·s)')

axes[0, 0].set_ylim(-80, 20)
axes[0, 1].set_ylim(0, 100)
axes[0, 2].set_ylim(0, .005)

plt.show()