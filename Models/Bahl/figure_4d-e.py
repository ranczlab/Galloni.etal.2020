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
gbar_nat_multiplier = np.linspace(0, 1, 5)


maxV_tuft = np.zeros([2, l.size, gbar_nat_multiplier.size])
maxV_trunk = np.zeros([2, l.size, gbar_nat_multiplier.size])
w_tuft = np.zeros([2, l.size, gbar_nat_multiplier.size])
w_trunk = np.zeros([2, l.size, gbar_nat_multiplier.size])
integral_trunk = np.zeros([2, l.size, gbar_nat_multiplier.size])
integral_tuft = np.zeros([2, l.size, gbar_nat_multiplier.size])

for i in range(l.size):
    h.apical.L = l[i]
   
    for j in range(gbar_nat_multiplier.size):
        
        h('recalculate_passive_properties()')
        h('''
            // See Keren et al. 2009

            soma distance()

            forsec apicaltree_list {
             for(x) gbar_kfast(x) = soma.gbar_kfast(0.5) * exp(-distance(x)/decay_kfast)
             for(x) gbar_kslow(x) = soma.gbar_kslow(0.5) * exp(-distance(x)/decay_kslow)
            }

            tuft mih = gbar_ih/distance(0)
            tuft mnat = (gbar_nat-soma.gbar_nat(0.5))/distance(0)

            apical for(x) gbar_nat(x) = (mnat*distance(x) + soma.gbar_nat(0.5))*%f
            apical for(x) gbar_ih(x) = mih*distance(x)
        ''' % gbar_nat_multiplier[j])
        h('recalculate_geometry()')
        
        print('multiplier: ' + str(gbar_nat_multiplier[j]))
        for seg in h.apical:
            print(seg.gbar_nat)
        # Simulate changing density of Na under 0 Ca2+
        h.tuft.gbar_sca = 0
        h.run()

        maxV_tuft[0, i, j] = np.max(np.array(tuft_v_vec))
        maxV_trunk[0, i, j] = np.max(np.array(apical_end_v_vec))

        w_trunk[0, i, j] = measure_width(apical_end_v_vec)
        w_tuft[0, i, j] = measure_width(tuft_v_vec)

        integral_trunk[0, i, j] = np.trapz(((np.array(apical_end_v_vec)[20000:25000] - apical_end_v_vec[15000]) / 10 ** 6), dx=0.025)
        integral_tuft[0, i, j] = np.trapz(((np.array(tuft_v_vec)[20000:25000] - tuft_v_vec[15000]) / 10 ** 6), dx=0.025)

        # Now simulate changing density of Na under original Ca2+
        h.tuft.gbar_sca = default_sca
        h.run()

        maxV_tuft[1, i, j] = np.max(np.array(tuft_v_vec))
        maxV_trunk[1, i, j] = np.max(np.array(apical_end_v_vec))

        w_trunk[1, i, j] = measure_width(apical_end_v_vec)
        w_tuft[1, i, j] = measure_width(tuft_v_vec)

        integral_trunk[1, i, j] = np.trapz(((np.array(apical_end_v_vec)[20000:25000] - apical_end_v_vec[15000]) / 10 ** 6), dx=0.025)
        integral_tuft[1, i, j] = np.trapz(((np.array(tuft_v_vec)[20000:25000] - tuft_v_vec[15000]) / 10 ** 6), dx=0.025)

trunk_colors = ['#eff3ff', '#bdd7e7', '#6baed6', '#3182bd', '#08519c']
tuft_colors = ['#fee5d9', '#fcae91', '#fb6a4a', '#de2d26', '#a50f15']

fig, axes = plt.subplots(3, 2, sharex='all', sharey='row', squeeze=False, figsize=(16, 16))

for i in range(gbar_nat_multiplier.size):
    axes[0, 0].plot(l, maxV_tuft[0, :, i], color=tuft_colors[i])
    axes[0, 0].plot(l, maxV_tuft[1, :, i], color=tuft_colors[i], linestyle='--')

    axes[0, 1].plot(l, maxV_trunk[0, :, i], color=trunk_colors[i])
    axes[0, 1].plot(l, maxV_trunk[1, :, i], color=trunk_colors[i], linestyle='--')

    axes[1, 0].plot(l, w_tuft[0, :, i], color=tuft_colors[i])
    axes[1, 0].plot(l, w_tuft[1, :, i], color=tuft_colors[i], linestyle='--')

    axes[1, 1].plot(l, w_trunk[0, :, i], color=trunk_colors[i])
    axes[1, 1].plot(l, w_trunk[1, :, i], color=trunk_colors[i], linestyle='--')

    axes[2, 0].plot(l, integral_tuft[0, :, i], color=tuft_colors[i])
    axes[2, 0].plot(l, integral_tuft[1, :, i], color=tuft_colors[i], linestyle='--')

    axes[2, 1].plot(l, integral_trunk[0, :, i], color=trunk_colors[i])
    axes[2, 1].plot(l, integral_trunk[1, :, i], color=trunk_colors[i], linestyle='--')

axes[0, 0].set_ylabel('peak voltage (mV)')
axes[1, 0].set_ylabel('width (ms)')
axes[2, 0].set_ylabel('integral (Vs)')

plt.savefig('outputs/figures/figure_4d-e.svg')