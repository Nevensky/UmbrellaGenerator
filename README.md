# UmbrellaGenerator
A script that generate Umbrella sampling simulation inputs for PLUMED/Gromacs and estimates free energies &amp; errors.


A set of scripts designed for generating Umbrella sampling inputs for PLUMED/Gromacs and analysing the resulting histograms to estimate the free energy curve and the associated statistical error using a modified Weighted Histogram Analysis Method (WHAM).<sup id="a1">[1](#f1)</sup> All histograms are block-averaged and WHAM results are checked for convergence.



<b id="f1">1.</b> Zhu, F. and Hummer, G. (2012), Convergence and error estimation in free energy calculations using the weighted histogram analysis method. J. Comput. Chem., 33: 453-465. doi:[10.1002/jcc.21989](http://doi.org/10.1002/jcc.21989). [↩](#a1)