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
tuft_ica_vec = h.Vector()
tuft_ica_vec.record(h.tuft(.5)._ref_ica)
t_vec = h.Vector()
t_vec.record(h._ref_t)

# Simulation parameters
dt = 0.025
h.tstop = 1000 - dt

width = np.linspace(0, 50, 20)
voltage = np.linspace(0, -70, 20)

burst = np.zeros([width.size, voltage.size])

for i in range(width.size):
    for j in range(voltage.size):
        stim.dur2 = width[i]
        stim.amp2 = voltage[j]
        h.run()

        ica = abs(np.min(np.array(tuft_ica_vec)))
        if ica > 0.01:
            burst[j, i] = 1
        else:
            burst[j, i] = 0

plt.imshow(burst, extent=[np.min(width), np.max(width), np.min(voltage), np.max(voltage)], cmap='Greys')
plt.xlabel('width (ms)')
plt.ylabel('peak voltage (mV)')
plt.show()