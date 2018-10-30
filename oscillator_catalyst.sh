#!/bin/bash

n=4
b=64
dt=0.05

echo "+ module load sensei/2.1.1-catalyst-shared"
module load sensei/2.1.1-catalyst-shared

set -x
mpiexec -n ${n} oscillator -b ${n} -t ${dt} -s ${b},${b},1 -g 1 \
    -f ./configs/random_2d_${b}_catalyst.xml ./configs/random_2d_${b}.osc
