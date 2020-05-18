from neuron import h
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.interpolate import UnivariateSpline

def find_changes(y):
    y /= np.std(y)
    threshold = 0.1

    m = y.size
    x = np.arange(m)
    s = m
    max_error = 1
    while max_error > threshold: 
        spl = UnivariateSpline(x, y, k=1, s=s)
        interp_y = spl(x)
        max_error = np.max(np.abs(interp_y - y))
        s /= 2
    knots = spl.get_knots()
    values = spl(knots)
    
    ts = knots.size
    idx = np.arange(ts)
    changes = []
    for j in range(1, ts-1):
        spl = UnivariateSpline(knots[idx != j], values[idx != j], k=1, s=0)
        if np.max(np.abs(spl(x) - interp_y)) > 2*threshold:
            changes.append(knots[j])
        
    return(changes[0])

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

Ih = np.arange(0, 1.1, .1)
l = np.arange(200, 610, 10)
array_size = [2, 2, l.size, Ih.size]  # Ca compartment length Ih
maxV = np.zeros(array_size)
w = np.zeros(array_size)
integral = np.zeros(array_size)

for i in range(l.size):

    h.apical.L = l[i]
    
    print('length: ' + str(h.apical.L))

    for j in range(Ih.size):

        for seg in h.tuft:
            seg.gbar_ih = 16.194815 * Ih[j]
            
        h('recalculate_channel_densities()')

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

fig, axes = plt.subplots(3, 2, sharex='all', sharey='row', squeeze=False, figsize=(16, 16))

for i in range(Ih.size):
    axes[0, 0].plot(l, maxV[0, 1, :, i])
    axes[0, 0].plot(l, maxV[1, 1, :, i], linestyle='--')

    axes[0, 1].plot(l, maxV[0, 0, :, i])
    axes[0, 1].plot(l, maxV[1, 0, :, i], linestyle='--')

    axes[1, 0].plot(l, w[0, 1, :, i])
    axes[1, 0].plot(l, w[1, 1, :, i], linestyle='--')

    axes[1, 1].plot(l, w[0, 0, :, i])
    axes[1, 1].plot(l, w[1, 0, :, i], linestyle='--')

    axes[2, 0].plot(l, integral[0, 1, :, i])
    axes[2, 0].plot(l, integral[1, 1, :, i], linestyle='--')

    axes[2, 1].plot(l, integral[0, 0, :, i])
    axes[2, 1].plot(l, integral[1, 0, :, i], linestyle='--')

axes[0, 0].set_ylabel('peak voltage (mV)')
axes[1, 0].set_ylabel('width (ms)')
axes[2, 0].set_ylabel('integral (Vs)')

axes[0, 0].set_ylim(-80, 20)
axes[1, 0].set_ylim(0, 120)
axes[2, 0].set_ylim(0, 0.006)
plt.savefig('outputs/figures/figure_4_supplementary_3b.svg')

critical_length = []
gradients = []

for i in range(Ih.size):
    x = l
    y = maxV[1, 1, :, i]
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    
    changes = find_changes(y)
    change_point = l[int(changes)]
    
    critical_length.append(change_point)
    gradients.append(z[0])
    
print('critical lengths: ' + str(critical_length))
print('gradients: ' + str(gradients))

with open(r'outputs/data/figure_4_supplementary_3b.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Ih', 'critical_length', 'slope'])
    for i in range(Ih.size):
        fields = [Ih[i], critical_length[i], gradients[i]]
        writer.writerow(fields)