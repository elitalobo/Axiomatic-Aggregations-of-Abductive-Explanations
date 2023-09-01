# aggrxp
Axiomatic Aggregations of Abductive Explanations (AXp's)



All datasets are available in *datasets/* folder.
Folders named *\*_ood* contain datasets for Lime attack.
Folders named *\*_shapood* contain datasets for SHAP attack.

To install all requirements of this code, run
```commandline
pip install -r requirements.txt
```

Before generating abductive explanations, an XGBoost model must be trained for the OOD classifier. To train an XGBoost model with T n_estimators, run
```commandline
python src/xreason.py -t -n T  datasets/traindataset.csv
```
This will generated a *temp/someotherpath/\*_mod.pkl* file.

As an example, you can run the following command to train an XGBoost model with T=100 on *compas_ood* dataset.

```commandline
python ../src/xreason.py -t -n 100 datasets/compas_ood/compas_ood.csv
```

Next, we need to create a file *datasets/dataset_name/config_num.yml* such that it contains information about the biased and unbiased features.
For an example, please check *datasets/compas_ood/config_num.yml*


To compute M abductive explanations for the predictions of the attack model with OOD classifier *temp/someotherpath/\*_mod.pkl* on a test dataset *somepath/testdataset.csv*, execute the following command.

```commandline
python src/xreason.py -v -e smt -s z3 --xnum M  -a datasets/dataset_name/config_num.yml temp/someotherpath/\*_mod.pkl somepath/testdataset.csv
```

For example, you can generate abductive explanations for the *compas_ood_small_test.csv* dataset by running the following command.
```commandline
python src/xreason.py -v -e smt -s z3 --xnum 100 -a datasets/compas_ood/config_num.yml temp/compas_ood/compas_ood_nbestim_100_maxdepth_3_testsplit_0.2.mod.pkl datasets/compas_ood/compas_ood_small_test.csv
```


The above step will generate a *mwc_expls.pkl* file containing all the abductive explanations. 
Suppose that the path to this file is *somepath1/mwc_expls.pkl*.
To generate feature importance weights using our methods - Responsibility index, Holler-Packel Index, Deegan-Packel Index, run

```commandline
python scripts/compute_explanations_single.py somepath1/mwc_expls.pkl "dataset_name"

```

For example, for the compas_ood dataset, the path to explanations file is "compas_ood_nbestim_100_maxdepth_3_testsplit_0.2.mod_nbestim_100_maxdepth_3_testsplit_0.2/mwc_expls.pkl" 
and the command for generating feature importance weights using our methods is

```commandline
python scripts/compute_explanations_single.py data/compas_ood_nbestim_100_maxdepth_3_testsplit_0.2.mod_nbestim_100_maxdepth_3_testsplit_0.2/mwc_expls.pkl "compas_ood"
```


All the explanation files generated in our experiments can be found in *data/* folder.


To replicate our results in the paper, run
```commandline
python adversarial_attack_results_agg.py
```

