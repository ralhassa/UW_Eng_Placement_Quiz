import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd
import pickle
from sklearn import metrics, tree, svm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold,cross_val_score,train_test_split,LeaveOneOut
from sklearn.naive_bayes import MultinomialNB
import csv
from datetime import datetime
import json
import pickle
import numpy as np
import sys
import itertools
import json
import numpy as np
import pandas as pd
import pickle
from statistics import mean
from sklearn import metrics, tree, svm, preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold,cross_val_score,train_test_split,LeaveOneOut
from sklearn.naive_bayes import MultinomialNB

# Changing questions into column headers for readability
READ_HEADERS = {
                'What Engineering program are you in?':'program',
                'Are you happy with what your program provides you with (i.e. courses, job opportunities, projects, etc.)':'happy',
                'What kind of problems do you enjoy solving?':'problem_type',
                'Would you consider yourself as being creative?':'creative',
                'What industry can you see yourself working in, in the future? Select all that apply.':'industry',
                'How comfortable are you working in the outdoors?':'outdoors',
                'What can you see yourself doing in the future?':'career',
                'How do you feel about group work? ':'group_work',
                'What high school class did you enjoy the most?':'liked_courses',
                'What high school class did you enjoy the least?':'disliked_courses',
                'How do you feel about computer programming?':'programming',
                'What type of club would you consider joining?':'join_clubs',
                'What type of club would you NOT want to join?':'not_clubs',
                'What project would you want to be a part of? ':'liked_projects',
                'What project do you find the least interesting?':'disliked_projects',
                'If you could only watch one TV show for the rest of your life, what would it be?':'tv_shows',
                'If engineering didn’t exist, what would you consider studying?':'alternate_degree',
                'How do you feel about working with expensive equipment?':'expensive_equipment',
                'How would you describe your drawing abilities?':'drawing',
                'You have an assignment to write an essay about anything you want. How does that make you feel?':'essay',
                "What is your gender?  **We're asking this to discover any gender biases in our questions**":'gender'
                }

READ_PROGRAMS = {
                'Mechanical Engineering':'mech',
                'Biomedical Engineering':'bmed',
                'Software Engineering':'swe',
                'Computer Engineering':'ce',
                'Mechatronics Engineering':'tron',
                'Civil Engineering':'cive',
                'Chemical Engineering':'chem',
                'Systems Design Engineering':'syde',
                'Management Engineering':'msci',
                'Electrical Engineering':'elec',
                'Nanotechnology Engineering':'nano',
                'Geological Engineering':'geo',
                'Environmental Engineering':'env',
                'Architectural Engineering':'arch-e',
                'Architecture':'arch'
                }

READ_PROBLEMS = {
                'Problems that are well defined.':'defined',
                'Problems that require some investigation.':'investigate',
                'Problems with very limited information.':'discover'
                }

READ_CREATIVE = {
                'I am somewhat creative.':'somewhat_creative',
                'I am not creative.' : 'not_creative',
                'I am very creative.' : 'creative'
                }

READ_INDUSTRY = {
                'Architecture (i.e. Designing a building taller than the CN Tower)':'architecture',
                'Automotive (i.e. Designing a new autonomous car)':'automotive',
                'Business (i.e. Starting your own consulting company)':'business',
                'Construction (i.e. Building a smart city)':'construction',
                'Health (i.e. Creating technology for minimally invasive surgeries)':'health',
                'Environment (i.e. Producing energy in sustainable ways)':'environment',
                'Manufacturing (i.e. Optimization or automation of manufacturing processes)':'manufacturing',
                'Technology (i.e. Working with cloud based software)':'technology'
                }

READ_OUTDOORS = {
                'Working outside would be okay, but only for short periods of time.':'limited',
                'I would rather work inside.':'indoors',
                'I love the outdoors and wish I could work outside every day.':'outdoors'
                }

READ_CAREERS = {
                'Building things with moving parts.':'moving_parts',
                'Designing or building sensor based technology.':'sensors',
                'Programming apps.':'programming',
                'Optimizing processes.':'optimizing',
                "Improving the way we use the world's resources.":'resources',
                'Designing buildings.':'buildings',
                'Making discoveries at the molecular level.':'molecules'
                }

READ_GROUPWORK = {
                'I occasionally like working with others.':'occasionally',
                'I enjoy working with others.':'yes',
                'I do not like working as part of a team. I would rather work alone.':'no'
                 }

READ_COURSES = {
                'Autoshop':'autoshop',
                'Biology':'biology',
                'Business':'business',
                'Chemistry':'chemistry',
                'Computer Science':'computer_science',
                'Geography':'geography',
                'History':'history',
                'Language Arts':'language_arts',
                'Math':'math',
                'Physics':'physics',
                'Visual Arts':'visual_arts'
                }

READ_PROGRAMMING = {
                    "I can code but it's not my favourite thing to do.":'partial',
                    "I code, I enjoy it and I'm good at it.":'complete',
                    'I don’t code and I have no desire to learn.':'no',
                    "I don't code but I am interested in trying it.":'interested'
                    }

READ_CLUBS = {
            'Art or design club (i.e. Fashion for Change)':'art/design',
            'Autoshop club (i.e. Autonomoose Autonomous Car Club)':'autoshop',
            'Business club (i.e. UW Finance Association)':'business',
            'Consulting club (i.e. DECA)':'consulting',
            'Environment club (i.e. UW Energy Network)':'environment',
            'Robotics club (i.e. UW Robotics Team)':'robotics',
            'Hacker club (i.e. UW Hacks)':'hacker_club',
            'Student council (i.e. Engineering Society)':'student_council',
            }

READ_PROJECTS = {
                'Prototyping a musical instrument for children with a disability.':'prototyping_instrument',
                'Designing a water treatment system for Mars.':'mars_water_treatment',
                'Programming a robot that can make you dinner.':'robot',
                'Building the world’s most powerful supercomputer.':'supercomputer',
                'Designing an Olympic village.':'olympic_village',
                'Creating a battery from recycled material.':'battery',
                'Optimizing the Uber Pool routes.':'uber_pool'
                }

READ_TV = {
            'Big Bang Theory':'big_bang_theory',
            'Breaking Bad':'breaking_bad',
            'Grey’s Anatomy':'greys_anatomy',
            'House Hunters':'house_hunters',
            'Myth Busters':'myth_busters',
            'Planet Earth':'planet_earth',
            'Silicon Valley':'silicon_valley'
            }

READ_ALTERNATE_DEGREE = {
            'Applied Science':'applied_science',
            'Business':'business',
            'Computer Science':'cs',
            'Economics':'econ',
            'English Literature':'lit',
            'Environmental Studies':'env',
            'Finance':'fin',
            'Geography':'geo',
            'Graphic Design':'design',
            'Health Studies':'health',
            'Marketing':'marketing',
            'Math':'math',
            'Political Science':'poli_sci',
            'Psychology':'psych',
            'Visual Arts':'visual_arts'
            }

READ_EQUIPMENT = {
            'That sounds cool!':'yes',
            "Could be cool, but I don't really care about fancy equipment or how much it costs.":'maybe',
            "That scares me and I don't want to touch it.":'no'
            }

READ_DRAWING = {
            'I am not the best, but I am not the worst.':'partial',
            'I am not very good.':'bad',
            'Really good, I can draw just about anything.':'good'
            }

READ_ESSAY = {
            'Excited! I can share my theories with the world.':'yes',
            'Annoyed. I would much rather be given a topic with clear instructions.':'no',
            'A bit apprehensive. I get overwhelmed with so many options.':'partial'
            }

INDEX_PROGRAM = {
                'mech': 9,
                'bmed': 2,
                'swe': 12,
                'tron': 14,
                'cive': 5,
                'chem': 4,
                'syde': 13,
                'msci': 10,
                'ce': 3,
                'elec': 6,
                'nano': 11,
                'geo': 8,
                'env': 7,
                'arch-e': 1,
                'arch': 0
                }
INV_INDEX_PROGRAM= {
            9:'mech',
            2:'bmed',
            12:'swe',
            14:'tron',
            5:'cive',
            4:'chem',
            13:'syde',
            10:'msci',
            3:'ce',
            6:'elec',
            11:'nano',
            8:'geo',
            7:'env',
            1:'arch-e',
            0:'arch'
            }
# Functions from data load

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
    try:
        data.new_programming = data.new_programming.map(READ_NEW_PROGRAMMING)
    except:
        print("new programming question not included")

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

def get_label_encoded_data(directory,model_name,column_list,drop_not_happy='H',data_balance=False,drop_gender=True):
    df = get_clean_data(directory,drop_not_happy,data_balance=data_balance,drop_gender=drop_gender)
    if drop_gender:
        df = df[column_list]
    else:
        column_list.append('gender')
        df = df[column_list]

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
            json.dump(str(row),f,cls=NpEncoder)

    with open('poc/quiz/exported_model_files/'+model_name+'_cols.txt', 'w') as f:
        for col in col_list:
            f.write(col)
            f.write('\n')

    return [df,encoded_dict_list]

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

def get_merged_encoded_data(directory,model_name,one_hot_encode,column_list,drop_not_happy='H',data_balance=False,drop_gender=True):
    df = get_label_encoded_data(directory,model_name,column_list,drop_not_happy,data_balance,drop_gender=drop_gender)[0]
    df = pd.get_dummies(df,columns=one_hot_encode)
    return df

def save_model(df,model,cat,model_name):
    df.to_csv ('poc/quiz/exported_model_files/'+model_name+'.csv', index = None, header=True)
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

# Define Parameters
MODEL_NAME = 'nb_ohe_f0_d0_b7_c36_v0'

d0 = 'poc/quiz/exported_model_files/d0.csv'

c36 = [
    'creative',
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

ohe =  [
        'creative',
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
        'essay'
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

b1 = {
    'mech': 100,
    'bmed': 100,
    'swe': 100,
    'tron': 100,
    'cive': 100,
    'chem': 100,
    'syde': 100,
    'msci': 100,
    'ce': 100,
    'elec': 100,
    'nano': 100,
    'geo': 100,
    'env': 100,
    'arch-e': 100,
    'arch': 100
    }


v0 = 1

#model_name = 'model-type_encoding_directory_datastructure_column-set_version'
# experiment_model_name = 'dataSet_dataBalance_columnSet_dataBalanceMultiple'
experiment_model_name = 'd0_b7_c36_v0'
directory = d0
data_balance = b7
column_list = c36
data_balance_multiple = v0 # Ratio of other programs to program in binary classifier. 2 means double of other programs, 0.5 means half

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

def sort_probability_dict(p_df):
    ordered_probabilties = sorted(p_df.values(),reverse=True)
    ordered_programs = sorted(p_df, key=p_df.get,reverse=True)
    return [p_df, ordered_probabilties, ordered_programs]

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

# Supporting Functions for RE-Building the model on the Heroku Server
print("building model...")
if 'le' in MODEL_NAME:
    # Building New model
    model_name = 'nb_le_f0_'+ experiment_model_name
    data = get_label_encoded_data(directory,model_name,column_list,'H',data_balance=data_balance)[0]

    x_df = data.drop(axis=1,columns=["program"])
    y_df = data["program"]

    X = np.array(x_df) # convert dataframe into np array
    Y = np.array(y_df) # convert dataframe into np array

    mnb = MultinomialNB()
    model = mnb.fit(X, Y) # fit the model using training data

    cat = data.drop('program',axis=1)
    cat = dict(zip(cat.columns,range(cat.shape[1])))

elif 'ohe' in MODEL_NAME:
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

# Scoring models
print("Scoring model")
model_name = model_name
temp_model_name = model_name

model_data = pd.read_csv('poc/quiz/exported_model_files/'+model_name+'.csv',dtype=str)
# Loading test data
if 'le' in model_name:
    test_data_t7 = get_label_encoded_data('poc/quiz/exported_model_files/t7.csv',model_name='t7',column_list=column_list,drop_not_happy='H',data_balance=False)[0]
elif 'ohe' in model_name:
    test_data_t7 = get_merged_encoded_data(directory = 'poc/quiz/exported_model_files/t7.csv',model_name ='t7',one_hot_encode=ohe,column_list = column_list,drop_not_happy='H',data_balance=False)

test_data_t7_temp = test_data_t7.copy()[list(model_data.columns)].head(210)

# Loading model files
pkl_file = open('poc/quiz/exported_model_files/'+model_name+'_cat', 'rb')
index_dict = pickle.load(pkl_file)
new_vector = np.zeros(len(index_dict))

pkl_file = open('poc/quiz/exported_model_files/'+model_name+'.pkl', 'rb')
model = pickle.load(pkl_file)

# Preparing Loading data
test_array = np.array(test_data_t7_temp.drop(axis=1,columns=["program"]))
test_actual = np.array(test_data_t7_temp["program"])

mclass_t3 = get_mclass_t3(temp_model_name,model,test_array,test_actual)
mclass_RR = get_mclass_rr(temp_model_name,model,test_array,test_actual)
mclass_accuracy = get_mclass_accuracy(temp_model_name,model,test_array,test_actual)

print("Model:  "+model_name)
print("t3:  "+str(mclass_t3))
print("RR:  "+str(mclass_RR))
print("Accuracy:  "+str(mclass_accuracy))
