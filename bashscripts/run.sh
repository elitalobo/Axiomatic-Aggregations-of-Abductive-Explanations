#! /bin/bash
#export MKL_NUM_THREADS=8
#export OPENBLAS_NUM_THREADS=8
#export OMP_NUM_THREADS=8

envs=("compas_ood" "compas_ood1" "compas_shapood" "compas_shapood1" "german_lmodified" "german_smodified" "compas_shapood" "compas_shapood1")
num=("100" "100" "100" "100" "50" "50" "50" "50")
for index in 0 1 2 3 4 5 6 7 8 9
do
    for id in 0 1 2 3 4 5 6 7
    do
               sbatch --time=04-01:00:00  --cpus-per-task=2 --ntasks-per-node=1 --mem-per-cpu=9000  --partition=longq  test_shap.sh  ${envs[id]} ${num[id]} $index
                           sbatch --time=04-01:00:00  --cpus-per-task=2 --ntasks-per-node=1 --mem-per-cpu=9000  --partition=longq  test_lime.sh  ${envs[id]} ${num[id]} $index
           done
       done
