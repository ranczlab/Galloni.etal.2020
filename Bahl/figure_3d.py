from neuron import h, gui
from matplotlib import pyplot as plt
import numpy as np

def g(X, Y):
    z = np.zeros(X.shape)
    for i in range(z[:, 0].size):
        h.apical.L = l[i]
        h('recalculate_passive_properties()')
        h('recalculate_channel_densities()')
        h('recalculate_geometry()')
        print('i: ' + str(i))
        for j in range(z[0, :].size):
            h.tuft.gbar_sca = sca[j]
            h.run()
            tuftv = np.array(tuft_v_vec)[20000:28000]
            z[i, j] = np.trapz(tuftv)
    return (z)

h.load_file('init_models_with_ca/init_model2.hoc')

soma_v_vec = h.Vector()
soma_v_vec.record(h.soma(0.5)._ref_v)
tuft_v_vec = h.Vector()
tuft_v_vec.record(h.tuft(0.5)._ref_v)

stim = h.IClamp(h.soma(0.5))
stim.amp = 1
stim.dur = 5
stim.delay = 500

stim_vec = h.Vector()
stim_vec.record(stim._ref_i)

epsp = h.epsp(h.tuft(0.5))
epsp.imax = 0.5
epsp.tau0 = 0.5
epsp.tau1 = 5
epsp.onset = 505

epsp_vec = h.Vector()
epsp_vec.record(epsp._ref_i)

t_vec = h.Vector() 
t_vec.record(h._ref_t)

simdur = 1000
dt = 0.025
h.tstop = simdur - dt

sca = np.linspace(0,1,10)
l = np.linspace(200,600,10)

X, Y = np.meshgrid(sca, l)
Z = g(X, Y)
np.save('outputs/data/figure_3d',Z)

plt.figure(figsize=(16,14))
plt.contourf(X, Y, Z, 1000)
plt.colorbar()
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel('trunk length', fontsize=40)
plt.xlabel('gCa', fontsize=40)
plt.savefig('outputs/figures/figure_3d.svg')