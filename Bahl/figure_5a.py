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
stim.dur2 = 20
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

cm = np.array([1, 2.5])
fig, axes = plt.subplots(2, cm.size, squeeze=False, sharex='all', sharey='all', figsize=(4, 4))

h.tuft.gbar_sca = 0
maxV = []

for i in range(cm.size):
    h.tuft.cm = cm[i]
    h.run()

    axes[0, i].plot(t_vec, tuft_v_vec, color='red')
    axes[1, i].plot(t_vec, apical_end_v_vec, color='blue')

    axes[0, i].set_title(str(cm[i]))

axes[0, 0].set_xlim(450, 650)
axes[0, 0].set_ylim(-80, -30)
plt.show()