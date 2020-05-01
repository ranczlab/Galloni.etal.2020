from neuron import h
from matplotlib import pyplot as plt
import numpy as np

def stimulate_cell(Is=1, Is_dur=5, Is_onset=100, Id_max=0.5, Id_rise=0.5, Id_decay=5, Id_onset=105, simdur=300,
                   dt=0.025, It=0, It_dur=5, It_onset=100, Ia=0, Ia_dur=5, Ia_onset=100, pulses_onset=100, pulses_dur=3,
                   pulses_amp=1.5, pulses_num=0, pulses_period=10):
    stim.amp, stim.dur, stim.delay = Is, Is_dur, Is_onset
    apical_stim.amp, apical_stim.dur, apical_stim.delay = Ia, Ia_dur, Ia_onset
    tuft_stim.amp, tuft_stim.dur, tuft_stim.delay = It, It_dur, It_onset
    epsp.imax, epsp.tau0, epsp.tau1, epsp.onset = Id_max, Id_rise, Id_decay, Id_onset
    pulses.delay, pulses.dur, pulses.per, pulses.num, pulses.amp = pulses_onset, pulses_dur, pulses_period, pulses_num, pulses_amp
    h.tstop = simdur - dt
    h.run()

h.load_file('init_models_with_ca/init_model2.hoc')

# Set up stimulus
stim = h.IClamp(h.soma(0.5))
epsp = h.epsp(h.tuft(0.5))
pulses = h.Ipulse2(h.soma(0.5))
apical_stim = h.IClamp(h.apical(.5))
tuft_stim = h.IClamp(h.tuft(.5))

# Set up recording vectors
soma_v_vec = h.Vector()
soma_v_vec.record(h.soma(0.5)._ref_v)
apical_v_vec = h.Vector()
apical_v_vec.record(h.apical(0.5)._ref_v)
tuft_v_vec = h.Vector()
tuft_v_vec.record(h.tuft(0.5)._ref_v)
stim_vec = h.Vector()
stim_vec.record(stim._ref_i)
epsp_vec = h.Vector()
epsp_vec.record(epsp._ref_i)
pulse_vec = h.Vector()
pulse_vec.record(pulses._ref_i)
apical_stim_vec = h.Vector()
apical_stim_vec.record(apical_stim._ref_i)
tuft_stim_vec = h.Vector()
tuft_stim_vec.record(tuft_stim._ref_i)
t_vec = h.Vector()
t_vec.record(h._ref_t)

l = np.linspace(600, 200, 2)

fig, axes = plt.subplots(2, l.size, sharex='all', sharey='row', squeeze=False, figsize=(16, 8))
for i in range(l.size):
    h.apical.L = l[i]
    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    #h('recalculate_geometry()')

    stimulate_cell(simdur=1000, Is_dur=5, Is=1, Is_onset=500, Id_max=0)

    axes[0, i].plot(t_vec, tuft_v_vec, color='red')
    axes[0, i].plot(t_vec, apical_v_vec, color='lightblue')
    axes[0, i].plot(t_vec, soma_v_vec, color='black')

    axes[0, i].set_xlim(450, 625)
    axes[0, i].set_ylim(-80, 50)

    axes[1, i].plot(t_vec, epsp_vec, color = 'red')
    axes[1, i].plot(t_vec, stim_vec, color = 'black')

axes[1, 0].set_ylim(-1, 3)
plt.savefig('outputs/figures/figure_3c_somaticonly.svg')


fig, axes = plt.subplots(2, l.size, sharex='all', sharey='row', squeeze=False, figsize=(16, 8))
for i in range(l.size):
    h.apical.L = l[i]
    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    #h('recalculate_geometry()')

    stimulate_cell(simdur=1000, Is=0, Id_max=.7, Id_onset=505)

    axes[0, i].plot(t_vec, tuft_v_vec, color='red')
    axes[0, i].plot(t_vec, apical_v_vec, color='lightblue')
    axes[0, i].plot(t_vec, soma_v_vec, color='black')

    axes[0, i].set_xlim(450, 625)
    axes[0, i].set_ylim(-80, 50)

    axes[1, i].plot(t_vec, epsp_vec, color = 'red')
    axes[1, i].plot(t_vec, stim_vec, color = 'black')

axes[1, 0].set_ylim(-1, 3)
plt.savefig('outputs/figures/figure_3c_epsponly.svg')

fig, axes = plt.subplots(2, l.size, sharex='all', sharey='row', squeeze=False, figsize=(16, 8))
for i in range(l.size):
    h.apical.L = l[i]
    h('recalculate_passive_properties()')
    h('recalculate_channel_densities()')
    #h('recalculate_geometry()')

    stimulate_cell(simdur=1000, Id_max=0.7, Is_onset=500, Id_onset=505)

    axes[0, i].plot(t_vec, tuft_v_vec, color='red')
    axes[0, i].plot(t_vec, apical_v_vec, color='lightblue')
    axes[0, i].plot(t_vec, soma_v_vec, color='black')

    axes[0, i].set_xlim(450, 625)
    axes[0, i].set_ylim(-80, 50)

    axes[1, i].plot(t_vec, epsp_vec, color = 'red')
    axes[1, i].plot(t_vec, stim_vec, color = 'black')

axes[1, 0].set_ylim(-1, 3)
plt.savefig('outputs/figures/figure_3c_BACfiring.svg')



