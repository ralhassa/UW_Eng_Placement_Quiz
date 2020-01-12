import json
import pandas as pd
import numpy as np
from sklearn import preprocessing

from dictionaries import *

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

def get_clean_data(directory,drop_not_happy):
    '''
    Should we drop "Are you happy with your program?"
    '''
    data = pd.read_csv(directory,dtype=str)
    # dropping PII + gender + skill_test + timestamp + year
    data = data.drop(data.columns[[0,1,3,4,24]], axis=1)

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
        binary_industry_data[col].values[:] = False

    for index, row in industry_data.iterrows():
        for i in range(8):
            try:
                binary_industry_data.iloc[int(index), binary_industry_data.columns.get_loc(row[i])] = 1
            except:
                error = "None_Type detected"

    data.index = data.index.map(int)
    binary_industry_data.index = binary_industry_data.index.map(int)
    data = (data.merge(binary_industry_data, left_on='id', right_on='id',how='left'))

    # if drop where all values are unhapppy
    if drop_not_happy:
        data = data[data.happy == 'Yes']
    return data

def get_encoded_data(directory):
    df = get_clean_data(directory)

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
        cd['column'] = col
        encoded_dict_list.append(cd)

    with open('encoded_dictionary', 'w') as file:
        file.write(json.dumps(encoded_dict_list, cls=NpEncoder))

    return [df,encoded_dict_list]

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

# def fix_industry
# fdf
'''
Might need these later

# def get_one_hot_encoded_data(directory):
#     df = get_clean_data(directory)
#     keys = df['current_average'].unique()
#     le = preprocessing.LabelEncoder()
#     le.fit(list(keys))
#     df['current_average'] = le.transform(list(df['current_average']))
#
#     df = pd.get_dummies(df)
#     return df
#
# def merged_encoding(directory,label_encode,one_hot_encode,drop_pref=False):
#
#     df = get_clean_data(directory)
#
#     if drop_pref == True:
#         df = df[df['current_average']!='Prefer not to say']
#
#     for col in label_encode:
#         keys = df[col].unique()
#         le = preprocessing.LabelEncoder()
#         le.fit(list(keys))
#         df[col] = le.transform(list(df[col]))
#
#     df = pd.get_dummies(df,columns=one_hot_encode)
#
#     return df
'''
