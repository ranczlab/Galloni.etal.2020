from neuron import h
import matplotlib.pyplot as plt
import numpy as np

def measure_width(trace):
    trace = np.array(trace)

    points = np.where(trace > (trace[15000] + 2))[0]
    points = points[np.logical_and(points >= 20000, points <= 30000)]

    width = dt * (points[-1] - points[0])

    return width

h.load_file('init_models_with_ca/init_model2.hoc')
default_sca = h.tuft.gbar_sca
default_cm = h.tuft.cm
default_apical_Ra = h.apical.Ra

# Set up stimulus
stim = h.Ipulse2(h.soma(.5))
stim.amp = 2
stim.dur = 3
stim.delay = 500
stim.per = 10
stim.num = 3

# Set up recording vectors
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

Ih = np.array([0, 0.25, 0.5, 0.75, 1])
l = np.array([200, 300, 400, 500, 600])
array_size = [2, 2, l.size, Ih.size]  # Ca compartment length Ih
maxV = np.zeros(array_size)
w = np.zeros(array_size)
integral = np.zeros(array_size)

for i in range(l.size):

    h.apical.L = l[i]

    for j in range(Ih.size):
        
        h('recalculate_passive_properties()')
        h('recalculate_channel_densities()')
        h('recalculate_geometry()')

        for seg in h.tuft:
            seg.gbar_ih = seg.gbar_ih * Ih[j]

        for seg in h.apical:
            seg.gbar_ih = seg.gbar_ih * Ih[j]

        h.tuft.gbar_sca = 0
        h.run()

        maxV[0, 0, i, j] = np.max(np.array(apical_end_v_vec))
        maxV[0, 1, i, j] = np.max(np.array(tuft_v_vec))

        w[0, 0, i, j] = measure_width(apical_end_v_vec)
        w[0, 1, i, j] = measure_width(tuft_v_vec)

        integral[0, 0, i, j] = np.trapz(((np.array(apical_end_v_vec)[20000:25000] - apical_end_v_vec[15000]) / 10 ** 6),
                                        dx=0.025)
        integral[0, 1, i, j] = np.trapz(((np.array(tuft_v_vec)[20000:25000] - tuft_v_vec[15000]) / 10 ** 6), dx=0.025)

        h.tuft.gbar_sca = default_sca
        h.run()

        maxV[1, 0, i, j] = np.max(np.array(apical_end_v_vec))
        maxV[1, 1, i, j] = np.max(np.array(tuft_v_vec))

        w[1, 0, i, j] = measure_width(apical_end_v_vec)
        w[1, 1, i, j] = measure_width(tuft_v_vec)

        integral[1, 0, i, j] = np.trapz(((np.array(apical_end_v_vec)[20000:25000] - apical_end_v_vec[15000]) / 10 ** 6),
                                        dx=0.025)
        integral[1, 1, i, j] = np.trapz(((np.array(tuft_v_vec)[20000:25000] - tuft_v_vec[15000]) / 10 ** 6), dx=0.025)

print(integral.shape)
trunk_colors = ['#eff3ff', '#bdd7e7', '#6baed6', '#3182bd', '#08519c']
tuft_colors = ['#fee5d9', '#fcae91', '#fb6a4a', '#de2d26', '#a50f15']

fig, axes = plt.subplots(3, 2, sharex='all', sharey='row', squeeze=False, figsize=(16, 16))

for i in range(Ih.size):
    axes[0, 0].plot(l, maxV[0, 1, :, i], color=tuft_colors[i])
    axes[0, 0].plot(l, maxV[1, 1, :, i], color=tuft_colors[i], linestyle='--')

    axes[0, 1].plot(l, maxV[0, 0, :, i], color=trunk_colors[i])
    axes[0, 1].plot(l, maxV[1, 0, :, i], color=trunk_colors[i], linestyle='--')

    axes[1, 0].plot(l, w[0, 1, :, i], color=tuft_colors[i])
    axes[1, 0].plot(l, w[1, 1, :, i], color=tuft_colors[i], linestyle='--')

    axes[1, 1].plot(l, w[0, 0, :, i], color=trunk_colors[i])
    axes[1, 1].plot(l, w[1, 0, :, i], color=trunk_colors[i], linestyle='--')

    axes[2, 0].plot(l, integral[0, 1, :, i], color=tuft_colors[i])
    axes[2, 0].plot(l, integral[1, 1, :, i], color=tuft_colors[i], linestyle='--')

    axes[2, 1].plot(l, integral[0, 0, :, i], color=trunk_colors[i])
    axes[2, 1].plot(l, integral[1, 0, :, i], color=trunk_colors[i], linestyle='--')

axes[0, 0].set_ylabel('peak voltage (mV)')
axes[1, 0].set_ylabel('width (ms)')
axes[2, 0].set_ylabel('integral (Vs)')

axes[0, 0].set_ylim(-80, 20)
axes[1, 0].set_ylim(0, 120)
axes[2, 0].set_ylim(0, 0.006)
plt.savefig('outputs/figures/figure_4_supplementary_3b.svg')