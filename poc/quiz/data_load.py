import itertools
import json
import numpy as np
import pandas as pd
import pickle
from sklearn import preprocessing

from . dictionaries import *

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

def transform_post_dict(post_dict):
    print("Transforming post_dict...")
    post_dict = json.dumps(dict(post_dict))
    post_dict = json.loads(post_dict)
    post_dict = dict(post_dict)
    industries = post_dict['industry']
    post_dict['architecture'] = '0'
    post_dict['automotive'] = '0'
    post_dict['business'] = '0'
    post_dict['construction'] = '0'
    post_dict['health'] = '0'
    post_dict['environment'] = '0'
    post_dict['manufacturing'] = '0'
    post_dict['technology'] = '0'
    for industry in industries:
        post_dict[industry] = '1'
    return dict(post_dict)

def get_encoded_data(directory,model_name,drop_not_happy):
    df = get_clean_data(directory,drop_not_happy)
    df = df.drop(['happy'], axis=1)

    col_list = list(df.columns)
    encoded_dict_list = []
    for col in col_list:
        keys = df[col].unique()
        le = preprocessing.LabelEncoder()
        le.fit(list(keys))
        df[col] = le.transform(list(df[col]))
        vals = df[col].unique()
        keys = list(le.inverse_transform(vals))
        cd = dict(zip(keys,vals))
        row = {str(col):cd}
        encoded_dict_list.append(row)
        with open('poc/quiz/exported_model_files/'+model_name+'_'+col+'_encoded_dictionary.json', 'w') as f:
            json.dump(row,f,cls=NpEncoder)

    with open('poc/quiz/exported_model_files/'+model_name+'_cols.txt', 'w') as f:
        for col in col_list:
            f.write(col)
            f.write('\n')

    return [df,encoded_dict_list]

def get_encoded_dict(model_name):
    cols = []
    with open('poc/quiz/exported_model_files/'+model_name+'_cols.txt', 'r') as f:
        for line in f:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            cols.append(currentPlace)
    encoded_dict = {}
    for col in cols:
        with open('poc/quiz/exported_model_files/'+model_name+'_'+col+'_encoded_dictionary.json', 'r') as f:
            row = json.loads(f.read())
        encoded_dict[col] = row
    return encoded_dict

def save_model(model,cat,model_name):
    with open('poc/quiz/exported_model_files/'+model_name+'.pkl', 'wb') as fid:
        pickle.dump(model, fid,2)
    with open('poc/quiz/exported_model_files/'+model_name+'_cat', 'wb') as fid:
        pickle.dump(cat, fid,2)

def retrieve_prediction_labels(model,prediction):
    # returns a dictionary for each label and their probability in the prediction
    labels = model.classes_
    results = prediction[0]
    results_dict = {}
    for i in range(len(results)):
        results_dict[INV_INDEX_PROGRAM[labels[i]]] = np.round(results[i],4)
    return results_dict

# Defining methods to help normaliz the data
def normalize_3_variables(df3,x,y,column,hue):
    normalized_data = df3[[x,y,column,hue]]
    normalized_data = normalized_data.groupby([x,y,column,hue],as_index=False).size().reset_index()
    normalized_data = normalized_data.rename(index=str,columns = {0:"percent"})
    normalized_data["percent"] = 100*(normalized_data["percent"]/sum(normalized_data["percent"]))
    return normalized_data

def normalize_2_variables(df2,x,y,column):
    normalized_data = df2[[x,y,column]]
    normalized_data = normalized_data.groupby([x,y,column],as_index=False).size().reset_index()
    normalized_data = normalized_data.rename(index=str,columns = {0:"percent"})
    normalized_data["percent"] = 100*(normalized_data["percent"]/sum(normalized_data["percent"]))
    return normalized_data

def normalize_1_variables(df1,x,y):
    normalized_data = df1[[x,y]]
    normalized_data = normalized_data.groupby([x,y],as_index=False).size().reset_index()
    normalized_data = normalized_data.rename(index=str,columns = {0:"percent"})
    normalized_data["percent"] = 100*(normalized_data["percent"]/sum(normalized_data["percent"]))
    return normalized_data

def heatmapify(df,one_var,list_one,two_var,list_two):
    return_list = []
    for one in list_one:
        new_list = []
        rez1 = df.loc[(df[one_var]==one)]
        for two in list_two:
            rez2 = rez1.loc[(rez1[two_var]==two)]
            if(len(rez2)>0):
                (new_list).append((float(rez2["percent"])))
            else:
                (new_list).append(0.0)
        (return_list).append((new_list))
    heatmapdf = pd.DataFrame(return_list, index=list_one, columns=list_two)
    return heatmapdf


def get_clean_data(directory,drop_not_happy='H',drop_gender=True,data_balance=False):
    '''
    Should we drop "Are you happy with your program?"
    '''
    data = pd.read_csv(directory,dtype=str)

    # dropping PII + skill_test + timestamp + year + raw_industry
    data = data.drop(data.columns[[0,1,3,24]], axis=1)

    # renaming data for readability
    data = data.rename(index=str,columns = READ_HEADERS)
    data.program = data.program.map(READ_PROGRAMS)
    data.problem_type = data.problem_type.map(READ_PROBLEMS)
    data.creative = data.creative.map(READ_CREATIVE)
    data.outdoors = data.outdoors.map(READ_OUTDOORS)
    data.career = data.career.map(READ_CAREERS)
    data.group_work = data.group_work.map(READ_GROUPWORK)
    data.liked_courses = data.liked_courses.map(READ_COURSES)
    data.disliked_courses = data.disliked_courses.map(READ_COURSES)
    data.programming = data.programming.map(READ_PROGRAMMING)
    data.join_clubs = data.join_clubs.map(READ_CLUBS)
    data.not_clubs = data.not_clubs.map(READ_CLUBS)
    data.liked_projects = data.liked_projects.map(READ_PROJECTS)
    data.disliked_projects = data.disliked_projects.map(READ_PROJECTS)
    data.tv_shows = data.tv_shows.map(READ_TV)
    data.alternate_degree = data.alternate_degree.map(READ_ALTERNATE_DEGREE)
    data.expensive_equipment = data.expensive_equipment.map(READ_EQUIPMENT)
    data.drawing = data.drawing.map(READ_DRAWING)
    data.essay = data.essay.map(READ_ESSAY)

    # Cleaning industry data
    data.index.name = 'id'
    industry_data = data["industry"].str.split(";", expand = True)
    industry_data = industry_data.replace(READ_INDUSTRY)
    binary_industry_data = np.array([np.arange(len(data))]*8).T
    binary_industry_data = pd.DataFrame(binary_industry_data, columns=READ_INDUSTRY.values())
    binary_industry_data.index.name = 'id'

    for col in binary_industry_data.columns:
        binary_industry_data[col].values[:] = '0'

    for index, row in industry_data.iterrows():
        for i in range(8):
            try:
                binary_industry_data.iloc[int(index), binary_industry_data.columns.get_loc(row[i])] = '1'
            except:
                error = "None_Type detected"

    data.index = data.index.map(int)
    binary_industry_data.index = binary_industry_data.index.map(int)
    data = (data.merge(binary_industry_data, left_on='id', right_on='id',how='left'))
    data = data.drop(['industry'], axis=1)

    # if drop where all values are unhapppy
    if drop_not_happy == 'H':
        data = data[data.happy == 'Yes']
        data = data.drop(['happy'], axis=1)
    if drop_not_happy == 'NH':
        data = data[data.happy == 'No']

    # drop gender data
    if drop_gender:
        data = data.drop(['gender'], axis=1)

    data.index = data.index.map(int)
    # data = data.sample(frac=1).reset_index(drop=True) ##Shuffle

    if data_balance != False:
        programs = list(READ_PROGRAMS.values())
        b_df = data.copy()
        b_df = b_df.head(0)

        for program in programs:
            temp_df = data.copy()[data.program==program]
            while len(temp_df) <= data_balance[program]:
                temp_df = temp_df.append(temp_df)
            temp_df = temp_df.head(data_balance[program])
            b_df = b_df.append(temp_df)
            b_df = b_df.reset_index(drop=True)
        data = b_df

    data.columns = data.columns.astype(str)
    return data

def transform_post_dict(post_dict):
    print("Transforming post_dict...")
    post_dict = json.dumps(dict(post_dict))
    post_dict = json.loads(post_dict)
    post_dict = dict(post_dict)
    industries = post_dict['industry']
    post_dict['architecture'] = '0'
    post_dict['automotive'] = '0'
    post_dict['business'] = '0'
    post_dict['construction'] = '0'
    post_dict['health'] = '0'
    post_dict['environment'] = '0'
    post_dict['manufacturing'] = '0'
    post_dict['technology'] = '0'
    for industry in industries:
        post_dict[industry] = '1'
    return dict(post_dict)

def get_label_encoded_data(directory,model_name,column_list,drop_not_happy='H',data_balance=False):
    print("getting label encoded data...")
    df = get_clean_data(directory,drop_not_happy,data_balance=data_balance)
    print("Retrieved label encodede data...")
    df = df[column_list]

    col_list = list(df.columns)
    encoded_dict_list = []
    print("encoding columns")
    for col in col_list:
        keys = df[col].unique()
        le = preprocessing.LabelEncoder()
        le.fit(list(keys))
        df[col] = le.transform(list(df[col]))
        vals = df[col].unique()
        keys = list(le.inverse_transform(vals))
        cd = dict(zip(keys,vals))
        row = {str(col):cd}
        encoded_dict_list.append(row)
        with open('poc/quiz/exported_model_files/'+model_name+'_'+col+'_encoded_dictionary.json', 'w') as f:
            json.dump(str(row),f,cls=NpEncoder)
    print("writing columns...")
    with open('poc/quiz/exported_model_files/'+model_name+'_cols.txt', 'w') as f:
        for col in col_list:
            f.write(col)
            f.write('\n')
    print("returning label encoded data...")
    return [df,encoded_dict_list]

def get_encoded_dict(model_name):
    cols = []

    with open('poc/quiz/exported_model_files/'+model_name+'_cols.txt', 'r') as f:
        for line in f:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            cols.append(currentPlace)
    encoded_dict = {}
    for col in cols:
        with open('poc/quiz/exported_model_files/'+model_name+'_'+col+'_encoded_dictionary.json', 'r') as f:
            row = json.loads(f.read())
        encoded_dict[col] = row
    return encoded_dict

def get_merged_encoded_data(directory,model_name,one_hot_encode,column_list,drop_not_happy='H',data_balance=False):
    print("getting merged encoded data...")
    df = get_label_encoded_data(directory,model_name,column_list,drop_not_happy,data_balance)[0]
    print("received merged encoded data...")
    df = pd.get_dummies(df,columns=one_hot_encode)
    return df
