import os

import pandas as pd

from utils import *


RESPONSIBILITY = "responsibility index"
HOLLER = "holler-packel index"
DEEGAN = "deegan-packel index"
LIME = "lime"
SHAP = "shap"

if __name__=='__main__':
    expl_dir = "data/"
    results={}
    for dir in os.listdir(expl_dir):
        dataset_name = "_".join(dir.split("_")[:2])
        n_estimators = dir.split("_")[3]
        name = dataset_name + " n_estimators=" + n_estimators
        if results.get(name) is None:
            results[name]={}
        for f in os.listdir(expl_dir + dir):
            if "mwc_expls" in f:
                f_path = expl_dir + dir + "/" + f
                # print("***************file_path***********",f_path)
                e_resp, e_holler, e_deegan = compute_abductive_explanations(dataset_name,f_path)
                results[name][RESPONSIBILITY]=e_resp
                results[name][HOLLER]= e_holler
                results[name][DEEGAN]=e_deegan

            elif "lime_expls" in f:
                f_path = expl_dir + dir + "/" + f
                # print("***************file_path***********", f_path)
                lime_exp = compute_lime_explanations(dataset_name, f_path)
                results[name][LIME]=lime_exp


            elif "shap_expls" in f:
                f_path = expl_dir + dir + "/" + f
                # print("***************file_path***********", f_path)
                shap_exp = compute_shap_explanations(dataset_name, f_path)
                results[name][SHAP]=shap_exp



            else:
                continue


for key, value in results.items():
    print("*****Dataset: " + key + "*********")
    for subkey , subvalue in value.items():
        print("Results for ",subkey)
        print(subvalue)


compas_imp_f = ['race','unrelated_column_one','unrelated_column_two']
german_imp_f= ['Gender', 'LoanRateAsPercentOfIncome']
methods_lime=[LIME, RESPONSIBILITY, HOLLER, DEEGAN]
methods_shap=[SHAP, RESPONSIBILITY, HOLLER, DEEGAN]

features_map={'race': 'Race', 'unrelated_column_one': 'UC1', 'unrelated_column_two': 'UC2', 'Gender': 'Gender', 'LoanRateAsPercentOfIncome':'LR'}
for key, value in results.items():
    if "compas" in key:
        imp_features = compas_imp_f
    else:
        imp_features = german_imp_f

    if "shap" in key or "smodified" in key:
        methods = methods_shap
    else:
        methods = methods_lime
    print("\n\nDataset: " + key)

    for f in imp_features:

        # print("Key and Methods", key, methods)
        line =  features_map[f] + " "
        for method in methods:
            res = results[key][method]

            for idx in range(3):
                try:
                    vals = res[idx+1]
                except:
                    print("####method", method)
                    print("###res", res)
                    line += " & " + str(0.0)
                    continue
                found=False
                for v in vals:
                    if v[0]==f:
                        line += " & " + str(round(v[1],3))
                        found=True
                        break
                if found==False:
                    line += " & " + str(0.0)

        print(line + " \\\\ ")





    print("\n\n")

