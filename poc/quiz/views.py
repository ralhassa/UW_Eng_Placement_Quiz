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
    program_set = Program.objects.all()
    description_set = Description.objects.all()
    comparison_set = Comparison.objects.all()
    course_set = Course.objects.all()
    career_set = Career.objects.all()
    context ={
            'program_set':program_set,
            'description_set':description_set,
            'comparison_set':comparison_set,
            'course_set':course_set,
            'career_set':career_set
            }
    return render(request,'quiz/programs.html',context)

def submit(request):
    try:
        print("Accessed submit...")
        if request.method == 'POST':
            print("Post method received")
            post_dict = request.POST
            print(post_dict)
            return response(request,post_dict)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return HttpResponse("Something went wrong...create) 3")

def recommendations(request,post_dict=False):
    if request.method == 'POST':
        context = {
            'response_message':'post'
        }
    else:
        context = {
            'response_message':'get'
        }
    return render(request,'quiz/recommendations.html',context)

def response(request,post_dict):
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
    # Need to create back-end to store results
    # new_record = Results()
    # new_record.name = post_dict['name']
    # new_record.email = post_dict['email']
    # new_record.OUTLOOK = post_dict['OUTLOOK']
    # new_record.TEMPERATURE = post_dict['TEMPERATURE']
    # new_record.HUMIDITY = post_dict['HUMIDITY']
    # new_record.WINDY = post_dict['WINDY']
    # new_record.PLAY = rm
    # # new_record.save()

    context = {
        'response_message':str(retrieve_prediction_labels(model,prediction)),
        'new_record':str()
    }
    print("Response Created...")
    return render(request,'quiz/response.html',context)

def download_to_csv(request):
    results = Results.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="quiz_data.csv"'

    writer = csv.writer(response)
    for result in results:
        writer.writerow([str(result)])

    return response
