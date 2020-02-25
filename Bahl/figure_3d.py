from neuron import h, gui
from matplotlib import pyplot as plt
import numpy as np


def stimulate_cell(Is=1, Is_dur=5, Is_onset=100, Id_max=0.5, Id_rise=0.5, Id_decay=5, Id_onset=105, simdur=300,
                   dt=0.025, It=0, It_dur=5, It_onset=100, Ia=0, Ia_dur=5, Ia_onset=100, pulses_onset=100, pulses_dur=3,
                   pulses_amp=1.5, pulses_num=0, pulses_period=10):
    stim.amp, stim.dur, stim.delay = Is, Is_dur, Is_onset
    epsp.imax, epsp.tau0, epsp.tau1, epsp.onset = Id_max, Id_rise, Id_decay, Id_onset
    h.tstop = simdur - dt
    h.run()


def g(X, Y):
    z = np.zeros(X.shape)
    for i in range(z[:, 0].size):
        h.apical.L = l[i]
        # h('recalculate_passive_properties()')
        # h('recalculate_channel_densities()')
        # h('recalculate_geometry()')
        print('i: ' + str(i))
        for j in range(z[0, :].size):
            h.tuft.gbar_sca = sca[j]
            stimulate_cell(Is_onset=500, Id_onset=505, simdur=1000)
            tuftv = np.array(tuft_v_vec)[20000:28000]
            z[i, j] = np.trapz(tuftv)
    return (z)

h.load_file('init_models_with_ca/init_model2.hoc')
soma_v_vec = h.Vector()
soma_v_vec.record(h.soma(0.5)._ref_v)
tuft_v_vec = h.Vector()
tuft_v_vec.record(h.tuft(0.5)._ref_v)
pulses = h.Ipulse2(h.soma(0.5))
pulse_vec = h.Vector()
pulse_vec.record(pulses._ref_i)

stim = h.IClamp(h.soma(0.5))
stim_vec = h.Vector()
stim_vec.record(stim._ref_i)
epsp = h.epsp(h.tuft(0.5))
epsp_vec = h.Vector()
epsp_vec.record(epsp._ref_i)

t_vec = h.Vector() 
t_vec.record(h._ref_t)

sca = np.linspace(0,1,10)
l = np.linspace(200,600,10)

X, Y = np.meshgrid(sca, l)
Z = g(X, Y)
np.save('gCa',Z)

plt.figure(figsize=(16,14))
plt.contourf(X, Y, Z, 1000, cmap='inferno')
plt.colorbar()
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel(r'trunk length ($\mu$m)', fontsize=40)
plt.xlabel(r'$\bar g_{Ca}$ mS/Cm$^2$', fontsize=40)
plt.show()