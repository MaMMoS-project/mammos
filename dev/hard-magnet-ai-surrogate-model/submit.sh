#!/bin/bash -l
#
# Standard output and error
#SBATCH -o ./job.out.%j
#SBATCH -e ./job.err.%j
#
# working directory
#SBATCH -D ./
#
# job name
#SBATCH -J ai-vs-mumag
#
# job requirements
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-task=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=128G
#SBATCH --partition=gpu
#
#SBATCH --mail-type=ALL
#SBATCH --mail-user=andrea.petrocchi@mpsd.mpg.de
#SBATCH --time=2-00:00:00

module purge
module load cuda/12.6

unset LD_LIBRARY_PATH

eval "$(pixi shell-hook)"
time python -u run.py
