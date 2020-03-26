import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd
import pickle
from sklearn import metrics, tree, svm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold,cross_val_score,train_test_split,LeaveOneOut
from sklearn.naive_bayes import MultinomialNB
from statistics import mean

from data_load import *
from dictionaries import *

def sort_probability_dict(p_df):
    ordered_probabilties = sorted(p_df.values(),reverse=True)
    ordered_programs = sorted(p_df, key=p_df.get,reverse=True)
    return [p_df, ordered_probabilties, ordered_programs]

def save_scores(scoring_dictionary,experiment_model_name):
    df = pd.DataFrame(scoring_dictionary)
    df = df.T
    df.to_csv("poc/quiz/exported_model_files/"+experiment_model_name+"_scores.csv", header=True)

def get_mclass_accuracy(temp_model_name,model,test_array,test_actual):
    test_pred = []
    for i in range(len(test_array)):
        test_pred.append(model.predict([test_array[i]]))
    accuracy = metrics.accuracy_score(test_pred,test_actual)
    return accuracy

def get_mclass_t3(temp_model_name,model,test_array,test_actual):
    t3_scores = []
    for i in range(len(test_array)):
        prediction = model.predict_proba([test_array[i]])
        probs = sort_probability_dict(retrieve_prediction_labels(model,prediction))[2][:3]
        n_probs = []
        for prob in probs:
            n_probs.append(INDEX_PROGRAM[prob])
        try:
            t3 = (1/(n_probs.index(test_actual[i])+1))
        except:
            t3 = 0
        t3_scores.append(t3)

    return mean(t3_scores)

def get_mclass_rr(temp_model_name,model,test_array,test_actual):
    rr_scores = []
    for i in range(len(test_array)):
        prediction = model.predict_proba([test_array[i]])
        probs = sort_probability_dict(retrieve_prediction_labels(model,prediction))[2]
        n_probs = []
        for prob in probs:
            n_probs.append(INDEX_PROGRAM[prob])
        try:
            rr = (1/(n_probs.index(test_actual[i])+1))
        except:
            rr = 0
        rr_scores.append(rr)
    return mean(rr_scores)
