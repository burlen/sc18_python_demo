#!/bin/bash

n=4
b=64
dt=0.05
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
bld=`echo -e '\e[1m'`
red=`echo -e '\e[31m'`
grn=`echo -e '\e[32m'`
blu=`echo -e '\e[36m'`
wht=`echo -e '\e[0m'`

mkdir -p ./configs
cp ${script_dir}/configs/* ./configs

echo "+ module use /usr/common/software/sensei/modulefiles"
module use /usr/common/software/sensei/modulefiles

echo "+ module load sensei/2.1.0-vtk-shared"
module load sensei/2.1.0-vtk-shared

set -x

cat ./configs/random_2d_${b}_python.xml | sed "s/.*/$blu&$wht/"

srun -n ${n} oscillator -b ${n} -t ${dt} -s ${b},${b},1 -p 0 \
    -f ./configs/random_2d_${b}_python.xml \
    ./configs/random_2d_${b}.osc  2>&1 | sed "s/.*/$red&$wht/"
