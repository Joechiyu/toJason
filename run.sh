#!/bin/bash
source activate /work/scratch/yuchi/miniconda3/envs/stats2
cd /home/students/yuchi/mean_shift
/work/scratch/yuchi/miniconda3/envs/stats2/bin/python /home/students/yuchi/mean_shift/mean_shift_test.py "$@"

