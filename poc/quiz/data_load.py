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

def get_clean_data(directory,drop_not_happy):
    '''
    Should we drop "Are you happy with your program?"
    '''
    data = pd.read_csv(directory,dtype=str)

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

    # if drop where all values are unhapppy
    if drop_not_happy:
        data = data[data.happy == 'Yes']
    data.index = data.index.map(int)
    # dropping PII + gender + skill_test + timestamp + year + raw_industry
    data = data.drop(data.columns[[0,1,3,4,8,24]], axis=1)
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
        with open('exported_model_files/'+model_name+'_'+col+'_encoded_dictionary.json', 'w') as f:
            json.dump(row,f,cls=NpEncoder)

    with open('exported_model_files/'+model_name+'_cols.txt', 'w') as f:
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
    with open('exported_model_files/'+model_name+'.pkl', 'wb') as fid:
        pickle.dump(model, fid,2)
    with open('exported_model_files/'+model_name+'_cat', 'wb') as fid:
        pickle.dump(cat, fid,2)

def retrieve_prediction_labels(model,prediction):
    # returns a dictionary for each label and their probability in the prediction
    labels = model.classes_
    results = prediction[0]
    results_dict = {}
    for i in range(len(results)):
        results_dict[INV_INDEX_PROGRAM[labels[i]]] = np.round(results[i],4)
    return results_dict

def check_skew(model_name, problem_type = True , creative = True, outdoors = True, career = True, group_work = True, liked_courses = True, disliked_courses = True, programming = True,join_clubs = True,not_clubs = True,liked_projects = True,disliked_projects = True,tv_shows = True,alternate_degree = True,expensive_equipment = True,drawing = True,essay = True,architecture = True,automotive = True,business = True,construction = True,health = True,environment = True,manufacturing = True,technology = True):
    encoded_dictionary = get_encoded_dict(model_name)

    problem_type = encoded_dictionary['problem_type']['problem_type']
    creative = encoded_dictionary['creative']['creative']
    outdoors = encoded_dictionary['outdoors']['outdoors']
    career = encoded_dictionary['career']['career']
    group_work = encoded_dictionary['group_work']['group_work']
    liked_courses = encoded_dictionary['liked_courses']['liked_courses']
    disliked_courses = encoded_dictionary['disliked_courses']['disliked_courses']
    programming = encoded_dictionary['programming']['programming']
    join_clubs = encoded_dictionary['join_clubs']['join_clubs']
    not_clubs = encoded_dictionary['not_clubs']['not_clubs']
    liked_projects = encoded_dictionary['liked_projects']['liked_projects']
    disliked_projects = encoded_dictionary['disliked_projects']['disliked_projects']
    tv_shows = encoded_dictionary['tv_shows']['tv_shows']
    alternate_degree = encoded_dictionary['alternate_degree']['alternate_degree']
    expensive_equipment = encoded_dictionary['expensive_equipment']['expensive_equipment']
    drawing = encoded_dictionary['drawing']['drawing']
    essay = encoded_dictionary['essay']['essay']
    architecture = encoded_dictionary['architecture']['architecture']
    automotive = encoded_dictionary['automotive']['automotive']
    business = encoded_dictionary['business']['business']
    construction = encoded_dictionary['construction']['construction']
    health = encoded_dictionary['health']['health']
    environment = encoded_dictionary['environment']['environment']
    manufacturing = encoded_dictionary['manufacturing']['manufacturing']
    technology = encoded_dictionary['technology']['technology']

    print("Loading..")
    test_variables = []
    if problem_type:
        test_variables.append(list(problem_type.values()))
    if creative:
        test_variables.append(list(creative.values()))
    if outdoors:
        test_variables.append(list(outdoors.values()))
    if career:
        test_variables.append(list(career.values()))
    if group_work:
        test_variables.append(list(group_work.values()))
    if liked_courses:
        test_variables.append(list(liked_courses.values()))
    if disliked_courses:
        test_variables.append(list(disliked_courses.values()))
    if programming:
        test_variables.append(list(programming.values()))
    if join_clubs:
        test_variables.append(list(join_clubs.values()))
    if not_clubs:
        test_variables.append(list(not_clubs.values()))
    if liked_projects:
        test_variables.append(list(liked_projects.values()))
    if disliked_projects:
        test_variables.append(list(disliked_projects.values()))
    if tv_shows:
        test_variables.append(list(tv_shows.values()))
    if alternate_degree:
        test_variables.append(list(alternate_degree.values()))
    if expensive_equipment:
        test_variables.append(list(expensive_equipment.values()))
    if drawing:
        test_variables.append(list(drawing.values()))
    if essay:
        test_variables.append(list(essay.values()))
    if architecture:
        test_variables.append(list(architecture.values()))
    if automotive:
        test_variables.append(list(automotive.values()))
    if business:
        test_variables.append(list(business.values()))
    if construction:
        test_variables.append(list(construction.values()))
    if health:
        test_variables.append(list(health.values()))
    if environment:
        test_variables.append(list(environment.values()))
    if manufacturing:
        test_variables.append(list(manufacturing.values()))
    if technology:
        test_variables.append(list(technology.values()))

    print('permutations')
    permutations = np.array(list(itertools.product(*test_variables)))
    print('permutations resolved')
    program_count = {
            'mech': 0,
            'bmed': 0,
            'swe': 10,
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

    print("Loading CAT file...")
    pkl_file = open('exported_model_files/'+model_name+'_cat', 'rb')
    index_dict = pickle.load(pkl_file)
    new_vector = np.zeros(len(index_dict))

    print("Loading model...")
    pkl_file = open('exported_model_files/'+model_name+'.pkl', 'rb')
    model = pickle.load(pkl_file)

    for p in permutations:
        p = np.array([p])
        result = INV_INDEX_PROGRAM[model.predict(p)[0]]
        program_count[result] = program_count[result] + 1

    return program_count

def test_model(model_name,vector):
    print("Loading CAT file...")
    pkl_file = open('exported_model_files/'+model_name+'_cat', 'rb')
    index_dict = pickle.load(pkl_file)
    new_vector = np.zeros(len(index_dict))

    print("Loading model...")
    pkl_file = open('exported_model_files/'+model_name+'.pkl', 'rb')
    model = pickle.load(pkl_file)
    prediction = model.predict_proba(vector)
    print("Results:")
    print(retrieve_prediction_labels(model,prediction))

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
