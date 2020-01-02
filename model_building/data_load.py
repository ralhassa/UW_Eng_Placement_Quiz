import json
import pandas as pd
import numpy as np
from sklearn import preprocessing

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
                'You have an assignment to write an essay about anything you want. How does that make you feel?':'essay'
                }

READ_PROGRAMS = {
                'Mechanical Engineering':'mech',
                'Biomedical Engineering':'bmed',
                'Software Engineering':'sft',
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

READ_OUTDOORS = {
                'Working outside would be okay, but only for short periods of time.':'limited',
                'I would rather work inside.':'indoors',
                'I love the outdoors and wish I could work outside every day.':'outdoors'
                }

READ_CAREERS = {
                'Building things with moving parts.':'building',
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
                'Computer Science':'computer_science',
                'Visual Arts' : 'visual_arts',
                'Language Arts':'language_arts'
                }

READ_PROGRAMMING = {
                    "I can code but it's not my favourite thing to do.":'partial',
                    "I code, I enjoy it and I'm good at it.":'complete',
                    'I don’t code and I have no desire to learn.':'no',
                    "I don't code but I am interested in trying it.":'interested'
                    }

READ_CLUBS = {
         'Robotics club (i.e. UW Robotics Team)':'robotics',
         'Student council (i.e. Engineering Society)':'student_council',
         'Consulting club or business club (i.e. DECA)':'consulting/business',
         'Environment club (i.e. UW Energy Network)':'environment',
         'Business club (i.e. UW Finance Association)':'business',
         'Hacker club (i.e. UW Hacks)':'hacker_club',
         'Autoshop club (i.e. Autonomoose Autonomous Car Club)':'autoshop',
         'Art or design club (i.e. Fashion for Change)':'art/design',
         'Consulting club (i.e. DECA)':'consulting'
            }

READ_PROJECTS = {
            'Designing a water treatment system for Mars.':'mars_water_treatment',
            'Prototyping a musical instrument for children with a disability.':'prototyping_instrument',
            'Programming a robot that can make you dinner.':'robot',
            'Optimizing the Uber Pool routes.':'uber_pool',
            'Designing an Olympic village.':'olympic_village',
            'Creating a battery from recycled material.':'battery',
            'Building the world’s most powerful supercomputer.':'supercomputer'
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

def get_clean_data(directory,drop_no):
    '''
    Should we drop "Are you happy with your program?"
    '''
    data = pd.read_csv(directory,dtype=str)
    # dropping PII + gender + skill_test + timestamp + year
    if drop_no:
        data = data.drop(data.columns[[0,1,3,4,24]], axis=1)
    else:
        data = data.drop(data.columns[[0,1,3,4,24]], axis=1)
    # renaming data for readability
    data = data.rename(index=str,columns = READ_HEADERS)
    data.program = data.program.map(READ_PROGRAMS)
    data.creative = data.creative.map(READ_CREATIVE)
    data.problem_type = data.problem_type.map(READ_PROBLEMS)
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
    data.expensive_equipment = data.expensive_equipment.map(READ_EQUIPMENT)
    data.drawing = data.drawing.map(READ_DRAWING)
    data.essay = data.essay.map(READ_ESSAY)

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
