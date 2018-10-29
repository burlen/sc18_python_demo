#!/bin/bash

n=4
b=64

echo "+ module load sensei/2.1.1-libsim-shared"
module load sensei/2.1.1-libsim-shared

set -x
mpiexec -np ${n} ADIOSAnalysisEndPoint -r flexpath \
    -f ./configs/random_2d_${b}_libsim.xml random_2d_${b}.bp

