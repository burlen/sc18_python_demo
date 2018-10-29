#!/bin/bash

n=4
b=64

echo "+ module load sensei/2.1.1-catalyst-shared"
module load sensei/2.1.1-catalyst-shared

set -x
mpiexec -np ${n} ADIOSAnalysisEndPoint -r flexpath \
    -f ./configs/random_2d_${b}_catalyst.xml random_2d_${b}.bp

