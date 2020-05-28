from neuron import h
import matplotlib.pyplot as plt
import numpy as np

h.load_file('init_models_with_ca/init_model2.hoc')
h.delete_section(sec=h.axon)
h.delete_section(sec=h.iseg)
h.delete_section(sec=h.hillock)

# Set up stimulus
stim = h.SEClamp(h.apical(1))
stim.amp1 = -70
stim.amp2 = -40
stim.amp3 = -70
stim.dur1 = 500
stim.dur2 = 10
stim.dur3 = 100

# Set up recording vectors
apical_end_v_vec = h.Vector()
apical_end_v_vec.record(h.apical(1)._ref_v)
tuft_v_vec = h.Vector()
tuft_v_vec.record(h.tuft(.5)._ref_v)
t_vec = h.Vector()
t_vec.record(h._ref_t)

# Simulation parameters
dt = 0.025
h.tstop = 1000 - dt

default_sca = h.tuft.gbar_sca

amps = np.array([-30, -54])
widths = np.array([10, 25])
fig, axes = plt.subplots(2, amps.size, squeeze=False, sharex='all', sharey='all', figsize=(4, 4))

for i in range(amps.size):
    
    stim.amp2 = amps[i]
    stim.dur2 = widths[i]

    h.tuft.gbar_sca = 0
    h.run()
    
    axes[0, i].plot(t_vec, tuft_v_vec, color='red')
    axes[1, i].plot(t_vec, apical_end_v_vec, color='blue')
    
    h.tuft.gbar_sca = default_sca
    h.run()
    
    axes[0, i].plot(t_vec, tuft_v_vec, color='red', linestyle = '--')
    axes[1, i].plot(t_vec, apical_end_v_vec, color='blue', linestyle = '--')

axes[0, 0].set_xlim(490, 580)
axes[0, 0].set_ylim(-80, 30)
plt.savefig('outputs/figures/figure_5c_i.svg')

amps = np.array([-7, -25])
widths = np.array([25, 35])
fig, axes = plt.subplots(2, amps.size, squeeze=False, sharex='all', sharey='all', figsize=(4, 4))

for i in range(amps.size):
    
    stim.amp2 = amps[i]
    stim.dur2 = widths[i]

    h.tuft.gbar_sca = 0
    h.run()
    
    axes[0, i].plot(t_vec, tuft_v_vec, color='red')
    axes[1, i].plot(t_vec, apical_end_v_vec, color='blue')
    
    h.tuft.gbar_sca = default_sca
    h.run()
    
    axes[0, i].plot(t_vec, tuft_v_vec, color='red', linestyle = '--')
    axes[1, i].plot(t_vec, apical_end_v_vec, color='blue', linestyle = '--')

axes[0, 0].set_xlim(490, 580)
axes[0, 0].set_ylim(-80, 30)
plt.savefig('outputs/figures/figure_5c_ii.svg')