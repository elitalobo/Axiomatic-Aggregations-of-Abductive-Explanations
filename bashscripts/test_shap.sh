#!/bin/bash

echo "/mnt/nfs/home/elitalobo/aggrxp/datasets/${1}/config.yml"

python /mnt/nfs/home/elitalobo/aggrxp/src/xreason_test.py -w -L 100 --xnum 100 -x -1.07,-0.48,-0.3,-1.03,0.99,0.99 -a "/mnt/nfs/home/elitalobo/aggrxp/datasets/${1}/config_num.yml" "/mnt/nfs/home/elitalobo/aggrxp/temp/${1}_${3}/${1}_${3}_nbestim_${2}_maxdepth_3_testsplit_0.2.mod.pkl" "/mnt/nfs/home/elitalobo/aggrxp/datasets/${1}_${3}/${1}_${3}_test.csv"



