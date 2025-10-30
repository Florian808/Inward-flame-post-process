# Overview
The scripts are split into two parts:
- "cluster" contains the scripts that are intended to run on the Euler cluster. They contain Job creation as well as post processing scripts to extract usable data from the raw Nek5000 checkpoints
- "local" contains the Jupyter notebooks that can be run locally.

Together, these scripts form a workflow from starting a simulation to visualising and plotting the results locally. In this workflow, the main steps are the following:
1. Create and compile a Nek5000 case.
2. Either submit manually or use the "job_submitter.py" script to start the simulation on the cluster.
3. After the computation has finished, use the "visit_post_process.py" script to extract isotherm and heat release data from the simulation.
4. Transfer the post-process results to the local machine.
5. Run the "Isocont_post_process.ipynb" notebook to plot the results.

## Submitting a job
Submitting a list of job can be done autimatically with the "job_submitter.py" script.
#### Requirements
- Loaded Python module on the cluster
- Compiled Nek5000 case named "inward". All parameters in the inward.par except the ones defined later (startFrom, numSteps, writeInterval, userParam01, userParam02) must be set, as they will not be adjusted by the script.

#### Prepare the job list
The list of jobs to be submitted needs to be prepared in a .csv file. An example file is located in "Cluster/Job_list_for_sub.csv". There, the following things need to be set for each job:
- "case": name of the case and name of the folder in which the Nek5000 casefiles are located.
- "velocity": inlet velocity at the inner boundary
- "run_number": can be any number identifying the simulation. Normally rising numbers from 1 within a choice of "case" and "velocity" make sense
- "startfrom": initial condition. There are several options available here:
  - "circ_\<_initial radius_\>": The flame is initialised circular with at an specified radius
  - "PC_\<_initial radius_\>\_\<_perturbation amplitude_\>\_\<_min perturbation mode_\>\_\<_max perturbation mode_\>": The flame is initialised circular and polychromatically perturbed at a specified mean radius. The pertubations amplitude as well as the range of modes [min;max] needs to be specified as well.
  - "\<case
  
## Post-processing a job on the cluster

## Running the notebook locally
