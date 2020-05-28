from neuron import h, gui
from matplotlib import pyplot as plt
import numpy as np

h.load_file('init_models_with_ca/init_model2.hoc')

stim = h.IClamp(h.soma(0.5))
stim_vec = h.Vector()
epsp = h.epsp(h.tuft(0.5))
epsp_vec = h.Vector()

tuft_v_vec = h.Vector()
tuft_v_vec.record(h.tuft(0.5)._ref_v)

tuft_ica_vec = h.Vector()
tuft_ica_vec.record(h.tuft(.5)._ref_ica)

t_vec = h.Vector() 
t_vec.record(h._ref_t)
dt = 0.025
h.tstop = 1000 - dt

epsp.tau0 = 0.5
epsp.tau1 = 5
stim.amp = 1
stim.dur = 5
stim.delay = 500

lengths = np.array([200, 300, 400, 500, 600])
allisyn = np.arange(0, 0.502, 0.02)
alldt = np.arange(-20, 21, 1)

burst = np.zeros([lengths.size, alldt.size, allisyn.size])
for i in range(lengths.size):
    length = lengths[i]
    h.apical.L = length
    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    h('recalculate_geometry()')
    for j in range(alldt.size):
        for k in range(allisyn.size):
            dt = alldt[j]
            isyn = allisyn[k]
            
            epsp.imax = isyn
            epsp.onset = 500 + dt
            
            h.run()
            
            tuftica = np.array(tuft_ica_vec )
            ica = abs(np.min(tuftica))
            if ica > 0.01:
                burst[i, j, k] = 1
            else:
                burst[i, j, k] = 0

fig, axes = plt.subplots(1, lengths.size, sharex='all', sharey='all', figsize=(16,4))
thresholds = np.zeros([lengths.size, alldt.size])
for i in range(lengths.size):
    for j in range(alldt.size):
        if np.count_nonzero(burst[i, j, :]) > 0:
            index = burst[i, j, :].argmax(axis=0)
            thresholds[i, j] = allisyn[index]
        else:
            thresholds[i, j] = np.nan
    axes[i].plot(alldt, thresholds[i, :], 'k.-')

plt.ylim(0, 0.5)
plt.xlim(-20, 20)

plt.savefig('outputs/figures/figure_3_supplementary_1e.svg')