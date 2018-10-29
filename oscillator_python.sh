#!/bin/bash

n=4
b=64
dt=0.1

echo "+ module load sensei/2.1.1-vtk-shared"
module load sensei/2.1.1-vtk-shared

set -x
mpiexec -n ${n} oscillator -b ${n} -t ${dt} -s ${b},${b},1  \
    -f ./configs/random_2d_${b}_python.xml ./configs/random_2d_${b}.osc
