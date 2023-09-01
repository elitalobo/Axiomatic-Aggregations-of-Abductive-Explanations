import os

import sys

import pandas as pd

from utils import *

if __name__=='__main__':
    path = sys.argv[1]
    dataset_name = sys.argv[2]

    if "mwc_expls" in path:


        compute_abductive_expls(dataset_name,path,data_path="datasets/")


    else:

        print("Not a valid explanations file")