import numpy as np
from neuron import h
from matplotlib import pyplot as plt

h.load_file('simulationcode/BAC_firing_long.hoc')

h('''
objref tuftica
access L5PC.apic[siteVec[0]]
tuftica = new Vector()
cvode.record(&ica(siteVec[1]),tuftica,tvec)''')

allisyn = np.arange(0, 0.502, 0.02)
alldt = np.arange(-20, 21, 1)
integral = np.zeros((alldt.size, allisyn.size))

fig, axes = plt.subplots(2, alldt.size, sharex = 'all', sharey = 'row', figsize=(16, 8))
burst = np.zeros([alldt.size, allisyn.size])
nspikes = np.zeros([alldt.size, allisyn.size])
for i in range(alldt.size):
    for j in range(allisyn.size):
        dt = alldt[i]
        isyn = allisyn[j]
        h.st1.amp = 1.9
        h.st1.dur = 5
        h.syn1.imax = isyn
        h.syn1.onset = 295 + dt
        h.run()

        tvec = np.array(h.tvec)
        vtuft = np.array(h.vdend2)
        tuftica = np.array(h.tuftica)
        
        vsoma = np.array(h.vsoma)
        vsoma[vsoma < 0] = 0
        vsoma[vsoma > 0] = 1
        nspikes[i, j] = np.sum(np.diff(vsoma) > 0)
        
        ica = abs(np.min(tuftica))
        if ica > 0.00125:
            burst[i, j] = 1
        else:
            burst[i, j] = 0

thresholds = [0] * alldt.size
for i in range(alldt.size):
    if np.count_nonzero(burst[i,:]) > 0:
        index = burst[i,:].argmax(axis=0)
        thresholds[i] = allisyn[index]
    else:
        thresholds[i] = np.nan

plt.figure()
plt.plot(alldt, thresholds ,'ko-')
plt.xlim(-20, 20)
plt.ylim(0, 0.5)
plt.savefig('outputs/figures/figure_3_supplementary_1a_long.svg.svg')