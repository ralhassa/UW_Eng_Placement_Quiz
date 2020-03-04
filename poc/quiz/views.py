import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import json
import pickle
import numpy as np
import sys

from . models import *
from . data_load import *
from . activate_model import *

def home(request):
    return render(request, 'quiz/home.html')

def quiz(request):
    return render(request, 'quiz/quiz.html')

def programs(request):
    recommendation_set = Recommendation.objects.all()
    comparison_set = Comparison.objects.all()
    context ={
            'recommendation_set':list(recommendation_set),
            'comparison_set':list(comparison_set)
            }
    return render(request,'quiz/programs.html',context)

def submit(request):
    try:
        print("Accessed submit...")
        if request.method == 'POST':
            print("Post method received")
            post_dict = request.POST
            print(post_dict)
            return recommendations(request,post_dict)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return HttpResponse("Something went wrong...create) 3")

def recommendations(request,post_dict):
    model_name = MODEL_NAME
    post_dict = transform_post_dict(post_dict)
    print("Entered Response Creation...")
    encoded_dictionary = get_encoded_dict(model_name)
    print("encoded_dictionary retrieved...")

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

    print("Labels encoded..")

	# Prepare the feature vector for prediction

    print("Loading new_vector....")
    pkl_file = open('poc/quiz/exported_model_files/'+model_name+'_cat', 'rb')
    index_dict = pickle.load(pkl_file)
    new_vector = np.zeros(len(index_dict))

    print("Loading response into new_vector...")
    new_vector[0] =  problem_type[post_dict['problem_type'][0]]
    new_vector[1] =  creative[post_dict['creative'][0]]
    new_vector[2] =  outdoors[post_dict['outdoors'][0]]
    new_vector[3] =  career[post_dict['career'][0]]
    new_vector[4] =  group_work[post_dict['group_work'][0]]
    new_vector[5] =  liked_courses[post_dict['liked_courses'][0]]
    new_vector[6] =  disliked_courses[post_dict['disliked_courses'][0]]
    new_vector[7] =  programming[post_dict['programming'][0]]
    new_vector[8] =  join_clubs[post_dict['join_clubs'][0]]
    new_vector[9] =  not_clubs[post_dict['not_clubs'][0]]
    new_vector[10] = liked_projects[post_dict['liked_projects'][0]]
    new_vector[11] = disliked_projects[post_dict['disliked_projects'][0]]
    new_vector[12] = tv_shows[post_dict['tv_shows'][0]]
    new_vector[13] = alternate_degree[post_dict['alternate_degree'][0]]
    new_vector[14] = expensive_equipment[post_dict['expensive_equipment'][0]]
    new_vector[15] = drawing[post_dict['drawing'][0]]
    new_vector[16] = essay[post_dict['essay'][0]]
    new_vector[17] = architecture[post_dict['architecture'][0]]
    new_vector[18] = automotive[post_dict['automotive'][0]]
    new_vector[19] = business[post_dict['business'][0]]
    new_vector[20] = construction[post_dict['construction'][0]]
    new_vector[21] = health[post_dict['health'][0]]
    new_vector[22] = environment[post_dict['environment'][0]]
    new_vector[23] = manufacturing[post_dict['manufacturing'][0]]
    new_vector[24] = technology[post_dict['technology'][0]]

    print("Loading model")
    pkl_file = open('poc/quiz/exported_model_files/'+model_name+'.pkl', 'rb')
    model = pickle.load(pkl_file)

    prediction = model.predict_proba([new_vector])
    print("Prediction created...")

    print("Creating new record...")
    new_record = Result()
    new_record.problem_type = post_dict['problem_type']
    new_record.creative = post_dict['creative']
    new_record.outdoors = post_dict['outdoors']
    new_record.career = post_dict['career']
    new_record.group_work = post_dict['group_work']
    new_record.liked_courses = post_dict['liked_courses']
    new_record.disliked_courses = post_dict['disliked_courses']
    new_record.programming = post_dict['programming']
    new_record.join_clubs = post_dict['join_clubs']
    new_record.not_clubs = post_dict['not_clubs']
    new_record.liked_projects = post_dict['liked_projects']
    new_record.disliked_projects = post_dict['disliked_projects']
    new_record.tv_shows = post_dict['tv_shows']
    new_record.alternate_degree = post_dict['alternate_degree']
    new_record.expensive_equipment = post_dict['expensive_equipment']
    new_record.drawing = post_dict['drawing']
    new_record.essay = post_dict['essay']
    new_record.architecture = post_dict['architecture']
    new_record.automotive = post_dict['automotive']
    new_record.business = post_dict['business']
    new_record.construction = post_dict['construction']
    new_record.health = post_dict['health']
    new_record.environment = post_dict['environment']
    new_record.manufacturing = post_dict['manufacturing']
    new_record.technology = post_dict['technology']
    new_record.save()

    # Getting Ordered Results
    results_dict = retrieve_prediction_labels(model,prediction)
    results = list(sorted(results_dict, key=lambda key: results_dict[key],reverse=True))
    return_list = []
    for key in results:
        return_list.append(Recommendation.objects.get(code=key))

    print("Weights of Results")
    print(results_dict)
    print("Response Created...")
    print(return_list)

    comparison_set = Comparison.objects.all()
    context ={
            'recommendation_set':return_list,
            'comparison_set':list(comparison_set)
            }
    return render(request,'quiz/recommendations.html',context)
