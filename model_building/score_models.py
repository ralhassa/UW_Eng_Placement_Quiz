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

def binary_predict_proba(vector,temp_model_name,test_data_t7):
    return_probabilities_dict = {}
    for program in list(INDEX_PROGRAM.keys()):
        # Loading data used to build the model
        model_name = temp_model_name+'_'+program
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        test_data_t7_temp = test_data_t7.copy()[list(model_data.columns)]

        # Converting program labels to their appropriate binary label BIN_CLAS
        temp_dictionary = INV_INDEX_PROGRAM.copy()
        for key in INV_INDEX_PROGRAM.keys():
            if str(key) != str(INDEX_PROGRAM[program]):
                temp_dictionary[key] = -1
            else:
                temp_dictionary[key] = INDEX_PROGRAM[program]
        test_data_t7_temp.program = test_data_t7_temp.program.map(temp_dictionary)

        # Loading model files
        pkl_file = open('exported_model_files/metadata/'+model_name+'_cat', 'rb')
        index_dict = pickle.load(pkl_file)
        new_vector = np.zeros(len(index_dict))

        pkl_file = open('exported_model_files/models/'+model_name+'.pkl', 'rb')
        model = pickle.load(pkl_file)

        return_probabilities_dict[program] = model.predict_proba([vector])[0][1]

    return (return_probabilities_dict)

def save_scores(scoring_dictionary,experiment_model_name):
    df = pd.DataFrame(scoring_dictionary)
    df = df.T
    df.to_csv("exported_model_files/scores/"+experiment_model_name+".csv", header=True)

def get_mclass_accuracy(temp_model_name,model,test_array,test_actual):
    test_pred = []
    for i in range(len(test_array)):
        test_pred.append(model.predict([test_array[i]]))
    accuracy = metrics.accuracy_score(test_pred,test_actual)
    return accuracy

def get_mclass_topN(temp_model_name,model,test_array,test_actual,topN):
    topN_scores = []
    for i in range(len(test_array)):
        prediction = model.predict_proba([test_array[i]])
        probs = sort_probability_dict(retrieve_prediction_labels(model,prediction))[2][:topN]
        if INV_INDEX_PROGRAM[test_actual[i]] in probs:
            topN_scores.append(1)
        else:
            topN_scores.append(0)
    return mean(topN_scores)

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

def get_mclass_reassignment(temp_model_name,model):
    # Reassignment Score for multi-label classifiers
    drop_gender = False
    directory = 'data/not_happy.csv'
    model_name = temp_model_name
    column_list = [
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
    m0 =  [
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

    m2 =  [
            'career',
            'liked_courses',
            'join_clubs',
            'alternate_degree'
            ]

    m3 =  [
            'career'
            ]

    m4 =  [
            'liked_courses'
            ]

    m5 =  [
            'join_clubs'
            ]

    m6 =  [
            'alternate_degree'
            ]

    m7 =  [
            'career',
            'liked_courses'
            ]

    m8 =  [
            'career',
            'join_clubs'
            ]

    m9 =  [
            'career',
            'alternate_degree'
            ]

    m10 =  [
            'liked_courses',
            'join_clubs'
            ]

    m11 =  [
            'liked_courses',
            'alternate_degree'
            ]

    m12 =  [
            'join_clubs',
            'alternate_degree'
            ]

    m13 =  [
            'career',
            'liked_courses',
            'join_clubs'
            ]

    m14 =  [
            'career',
            'join_clubs',
            'alternate_degree'
            ]

    m15 =  [
            'career',
            'liked_courses',
            'alternate_degree'
            ]

    m16 =  [
            'liked_courses',
            'join_clubs',
            'alternate_degree'
            ]

    # Loading unhappy data
    if 'le' in model_name:
        tG_df = get_label_encoded_data(directory=directory,model_name=model_name,column_list=column_list,drop_not_happy='NH',data_balance=False)[0]
        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)

        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'ohe' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=ohe,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm0' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m0,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm2' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m2,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm3' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m3,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm4' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m4,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm5' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m5,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm6' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m6,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm7' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m7,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm8' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m8,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm9' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m9,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm10' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m10,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm11' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m11,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm12' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m12,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm13' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m13,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm14' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m14,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm15' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m15,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'm16' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=m16,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    # Preparing unhappy data to be consumed by the model
    test_array = np.array(tG_df.drop(axis=1,columns=["program"]))
    test_actual = np.array(tG_df["program"])
    test_pred = []

    for i in range(len(test_array)):
        test_pred.append(model.predict([test_array[i]]))

    reassignment = 1 - metrics.accuracy_score(test_pred,test_actual)

    return reassignment

def get_bclass_accuracy(test_array,model_name,test_actual,test_data_t7):
    test_pred = []
    for i in range(len(test_array)):
        predicted = INDEX_PROGRAM[sort_probability_dict(binary_predict_proba(test_array[i],model_name,test_data_t7))[2][0]]
        test_pred.append(predicted)

    accuracy = metrics.accuracy_score(test_pred,test_actual)

    return accuracy

def get_bclass_t3(test_array,model_name,test_actual,test_data_t7):
    t3_scores = []
    for i in range(len(test_array)):
            probs = sort_probability_dict(binary_predict_proba(test_array[i],model_name,test_data_t7))[2][:3]
            n_probs = []
            for prob in probs:
                n_probs.append(INDEX_PROGRAM[prob])
            try:
                t3 = ((1/(n_probs.index(test_actual[i])+1)))
            except:
                t3 = 0
            t3_scores.append(t3)

    return mean(t3_scores)

def get_bclass_rr(test_array,model_name,test_actual,test_data_t7):
    rr_scores = []

    for i in range(len(test_array)):
            probs = sort_probability_dict(binary_predict_proba(test_array[i],model_name,test_data_t7))[2]
            n_probs = []
            for prob in probs:
                n_probs.append(INDEX_PROGRAM[prob])
            try:
                rr = (1/(n_probs.index(test_actual[i])+1))
            except:
                rr = 0
            rr_scores.append(rr)

    return mean(rr_scores)

def get_bclass_reassignment(test_array,model_name,test_data_t7):
    # Reassignment Score for multi-label classifiers
    drop_gender = False
    directory = 'data/not_happy.csv'
    column_list = [
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

    # Loading unhappy data
    if 'le' in model_name:
        tG_df = get_label_encoded_data(directory=directory,model_name=model_name,column_list=column_list,drop_not_happy='NH',data_balance=False)[0]
        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)

        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    elif 'ohe' in model_name:
        tG_df = get_merged_encoded_data(directory = directory,model_name =model_name,one_hot_encode=ohe,column_list = column_list,drop_not_happy='NH',data_balance=False)

        tG_df = tG_df.reset_index()
        tG_df = tG_df.drop(['id'], axis=1)
        model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
        tG_df = tG_df[list(model_data.columns)].head(30)

    # Preparing unhappy data to be consumed by the model
    test_array = np.array(tG_df.drop(axis=1,columns=["program"]))
    test_actual = np.array(tG_df["program"])
    test_pred = []

    for i in range(len(test_array)):
        predicted = INDEX_PROGRAM[sort_probability_dict(binary_predict_proba(test_array[i],model_name,test_data_t7))[2][0]]
        test_pred.append(predicted)

    reassignment = 1 - metrics.accuracy_score(test_pred,test_actual)

    return reassignment

def check_gender_bias(directory,model_name,column_list):
    drop_gender=False

    gender_data = get_clean_data(directory,drop_gender=drop_gender)[['program','gender']]
    gender_data = gender_data.reset_index()
    gender_data = gender_data.drop(['id'], axis=1)

    test_data = get_encoded_data(directory,model_name)[0]
    test_data = test_data[column_list]
    test_data = test_data.reset_index()
    test_data = test_data.drop(['program','id'], axis=1)

    pkl_file = open('exported_model_files/metadata/'+model_name+'_cat', 'rb')
    index_dict = pickle.load(pkl_file)
    new_vector = np.zeros(len(index_dict))

    pkl_file = open('exported_model_files/models/'+model_name+'.pkl', 'rb')
    model = pickle.load(pkl_file)

    predictions ={}
    for i in range(0,len(test_data)):
        vector = np.asarray(test_data.loc[i,])
        vector = np.array(vector).reshape(1, -1)
        predictions[i] = INV_INDEX_PROGRAM[model.predict(vector)[0]]

    gender_data['predicted_program'] = pd.Series(predictions)
    gender_count = {}
    for i in range(0,len(gender_data)):
        try:
            program_count = gender_count[gender_data.loc[i,'gender']]
            try:
                program_count[gender_data.loc[i,'predicted_program']] =program_count[gender_data.loc[i,'predicted_program']] + 1
            except:
                program_count[gender_data.loc[i,'predicted_program']] = 0

            gender_count[gender_data.loc[i,'gender']] = program_count
        except:
            gender_count[gender_data.loc[i,'gender']] = {
                                                            'mech': 0,
                                                            'bmed': 0,
                                                            'swe': 0,
                                                            'tron': 0,
                                                            'cive': 0,
                                                            'chem': 0,
                                                            'syde': 0,
                                                            'msci': 0,
                                                            'ce': 0,
                                                            'elec': 0,
                                                            'nano': 0,
                                                            'geo': 0,
                                                            'env': 0,
                                                            'arch-e': 0,
                                                            'arch': 0
                                                            }
            program_count = gender_count[gender_data.loc[i,'gender']]
            try:
                program_count[gender_data.loc[i,'predicted_program']] =program_count[gender_data.loc[i,'predicted_program']] + 1
            except:
                program_count[gender_data.loc[i,'predicted_program']] = 0
            gender_count[gender_data.loc[i,'gender']] = program_count
    return gender_count
