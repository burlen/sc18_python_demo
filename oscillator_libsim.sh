#!/bin/bash

n=4
b=64
dt=0.2

echo "module load sensei/2.1.1-libsim-shared"
module load sensei/2.1.1-libsim-shared

set -x

mpiexec -n ${n} oscillator -b ${n} -t ${dt} -s ${b},${b},1 -g 1 \
    -f ./configs/random_2d_${b}_libsim.xml ./configs/random_2d_${b}.osc
