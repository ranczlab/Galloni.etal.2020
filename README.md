# Data and models of length-dependent Ca<sup>2+</sup> electrogenesis in layer 5 pyramidal neurons

This repository reproduces figures from "Apical length governs computational diversity of layer 5 pyramidal neurons" (Galloni et al., 2020) available as a [preprint](https://www.biorxiv.org/content/10.1101/754499v2) and submitted for publication.

### Prerequisites

Figures from physiological experiments were originally generated in MATLAB R2018a and should be compatible with later versions. 

Modelling experiments were originally written in Python 3.6 and make use of the SciPy library (http://scipy.org) and the NEURON simulation environment (7.7.1, http://neuron.yale.edu). Please refer to respective documentation for further instructions.

### File structure

* **Experiments**
  + data
  + scripts
* **Models**
  + ***Bahl***
    + outputs
      + figures
      + data
    + ...
  + ***Hay***
    + outputs
      + figures
      + data
    + ...

The /Experiments directory contains experimental data and scripts for generating figures 1 and 2 (and related supplementary figures). The scripts were originally written for MATLAB R2018a.

The /Models directory contains separate sub-directories for the Hay et al. (2011) and Bahl et al. (2012) models. When code for these models is run, the /outputs sub-directory will be populated with simulated data and figures. The /outputs sub-directories are empty by default to reduce storage requirements.

The /Bahl sub-directory contains code for the reduced model based on the same by Bahl et al. (2012). Figures related to the reduced model are reproducible through the Python scripts (running Python 3.6).

The /Hay sub-directory contains code for the detailed (morphologically realistic) model based on the original by Hay et al. (2011). Figures related to the detailed model require manual editing of the base files associated with the model in order to fully reproduce the figures in the paper. The shell script in the parent directory automates this process. A full account of parameters used is available in the submission.
