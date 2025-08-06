#!/bin/bash
#PBS -N Nvidia_SMI                                                                                            
#PBS -q gpu                                                         
#PBS -l select=1:ncpus=10:ngpus=2:mem=32g                           
#PBS -j oe                                                          
#PBS -V                                                             

cd $PBS_O_WORKDIR                                                   # Go to the directory where the job was submitted
source /home/soft/anaconda3/etc/profile.d/conda.sh                  # Set up conda
conda init                                                          # Initialize conda (optional)
conda activate mayank_venv                                        # Activate your conda environment
module load cuda                                                    # Load CUDA (needed for GPU code)
nvidia-smi                                                      # Check GPU status
