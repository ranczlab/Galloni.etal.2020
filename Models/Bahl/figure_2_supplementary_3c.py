from neuron import h, gui
from matplotlib import pyplot as plt
import numpy as np
import csv
from os import path

h.load_file('init_models_with_ca/init_model2.hoc')

soma_v_vec = h.Vector()
soma_v_vec.record(h.soma(0.5)._ref_v)

stim = h.IClamp(h.soma(0.5))
stim_vec = h.Vector()
stim_vec.record(stim._ref_i)

t_vec = h.Vector() 
t_vec.record(h._ref_t)
dt = 0.025
h.tstop = 1500 - dt

stim.dur = 500
stim.delay = 500

lengths = np.array([200, 300, 400, 500, 600])
fig, axes = plt.subplots(2, lengths.size, squeeze = False, sharex = 'all', sharey = 'row', figsize = (16, 8))

amps = np.arange(-0.4, 0.62, .02)
for i in range(lengths.size):
    h.apical.L = lengths[i]
    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    h('recalculate_geometry()')
    
    for j in range(amps.size):
        stim.amp = amps[j]
        h.run()
        
        axes[0, i].plot(t_vec, soma_v_vec)
        axes[1, i].plot(t_vec, stim_vec)

        fields = np.array([lengths[i], amps[j], np.array(soma_v_vec)])
        
        details = np.array([lengths[i], amps[j]])
        vsoma = np.array(soma_v_vec)
        fields = np.append(details, vsoma)

        if path.exists('outputs/data/figure_2_supplementary_3c.csv'):
            with open(r'outputs/data/figure_2_supplementary_3c.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
        else:
            with open(r'outputs/data/figure_2_supplementary_3c.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['lengths', 'input'] + list(t_vec))
                writer.writerow(fields)
            
axes[0,0].set_ylim(-150, 70)
plt.xlim(300, 1200)
plt.savefig('figure_2_supplementary_3c.svg')