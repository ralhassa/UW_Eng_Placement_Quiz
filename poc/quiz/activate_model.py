import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd
import pickle
from sklearn import metrics, tree, svm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold,cross_val_score,train_test_split,LeaveOneOut
from sklearn.naive_bayes import MultinomialNB

from . data_load import *
from . dictionaries import *

# Define Parameters
MODEL_NAME = 'nb_ohe_f0_d0_b7_c36_v0'

def main():
    d0 = 'poc/quiz/exported_model_files/d0.csv'

    c36 = ['creative',
           'outdoors',
           'career',
           'group_work',
           'liked_courses',
           'disliked_courses',
           'join_clubs',
           'not_clubs',
           'liked_projects',
           'disliked_projects',
           'alternate_degree',
           'drawing',
           'essay',
           'architecture',
           'automotive',
           'business',
           'construction',
           'health',
           'environment',
           'manufacturing',
           'technology',
           'program'
    ]

    b0 = False # this is only relevant when we want to use untreated data for code d0

    b7 = {
        'mech': 100,
        'bmed': 100,
        'swe': 100,
        'tron': 100,
        'cive': 100,
        'chem': 100,
        'syde': 100,
        'msci': 100,
        'ce': 40,
        'elec': 100,
        'nano': 100,
        'geo': 100,
        'env': 100,
        'arch-e': 100,
        'arch': 100
        }

    v0 = 1

    ohe =  [
            'problem_type',
            'creative',
            'outdoors',
            'career',
            'group_work',
            'liked_courses',
            'disliked_courses',
            'programming',
            'join_clubs',
            'not_clubs',
            'liked_projects',
            'disliked_projects',
            'tv_shows',
            'alternate_degree',
            'expensive_equipment',
            'drawing',
            'essay'
            ]

    ohe = [value for value in ohe if value in  column_list]

    #model_name = 'model-type_encoding_directory_datastructure_column-set_version'
    # experiment_model_name = 'dataSet_dataBalance_columnSet_dataBalanceMultiple'
    experiment_model_name = 'd0_b7_c36_v0'
    directory = d0
    data_balance = b7
    column_list = c36
    data_balance_multiple = v0 # Ratio of other programs to program in binary classifier. 2 means double of other programs, 0.5 means half




    # Supporting Functions for RE-Building the model on the Heroku Server

    # Building New model
    model_name = 'nb_ohe_f0_'+ experiment_model_name
    data = get_merged_encoded_data(directory,model_name,one_hot_encode=ohe,column_list = column_list,drop_not_happy='H',data_balance=data_balance)

    x_df = data.drop(axis=1,columns=["program"])
    y_df = data["program"]

    X = np.array(x_df) # convert dataframe into np array
    Y = np.array(y_df) # convert dataframe into np array

    mnb = MultinomialNB()
    model = mnb.fit(X, Y) # fit the model using training data

    cat = data.drop('program',axis=1)
    cat = dict(zip(cat.columns,range(cat.shape[1])))

    save_model(data,model,cat,model_name)

if __name__ == '__main__':
    main()
