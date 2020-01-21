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

def index(request):
    return HttpResponse("This is the home page")

def form(request):
    return render(request, 'quiz/form.html')

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

def response(request,post_dict):
    model_name = MODEL_NAME
    print("Entered Response Creation...")
    encoded_dictionary = get_encoded_dict(model_name)
    print("encoded_dictionary retrieved...")

    problem_type = encoded_dictionary['problem_type']
    print(1)
    creative = encoded_dictionary['creative']
    print(2)
    outdoors = encoded_dictionary['outdoors']
    print(3)
    career = encoded_dictionary['career']
    print(4)
    group_work = encoded_dictionary['group_work']
    print(5)
    liked_courses = encoded_dictionary['liked_courses']
    print(6)
    disliked_courses = encoded_dictionary['disliked_courses']
    print(7)
    programming = encoded_dictionary['programming']
    print(8)
    join_clubs = encoded_dictionary['join_clubs']
    print(9)
    not_clubs = encoded_dictionary['not_clubs']
    print(10)
    liked_projects = encoded_dictionary['liked_projects']
    print(11)
    disliked_projects = encoded_dictionary['disliked_projects']
    print(12)
    tv_shows = encoded_dictionary['tv_shows']
    print(13)
    alternate_degree = encoded_dictionary['alternate_degree']
    print(14)
    expensive_equipment = encoded_dictionary['expensive_equipment']
    print(15)
    drawing = encoded_dictionary['drawing']
    print(16)
    essay = encoded_dictionary['essay']
    print(17)
    architecture = encoded_dictionary['architecture']
    print(18)
    automotive = encoded_dictionary['automotive']
    print(19)
    business = encoded_dictionary['business']
    print(20)
    construction = encoded_dictionary['construction']
    print(21)
    health = encoded_dictionary['health']
    print(22)
    environment = encoded_dictionary['environment']
    print(23)
    manufacturing = encoded_dictionary['manufacturing']
    print(24)
    technology = encoded_dictionary['technology']

    print("Labels encoded..")

	# Prepare the feature vector for prediction

    print("Loading new_vector....")
    pkl_file = open('poc/quiz/exported_model_files/'+model_name+'_cat', 'rb')
    index_dict = pickle.load(pkl_file)
    new_vector = np.zeros(len(index_dict))

    print("Loading response into new_vector...")
    print(post_dict['problem_type'])
    print()
    print(problem_type)
    new_vector[0] =  problem_type[post_dict['problem_type']]
    print(1)
    new_vector[1] =  creative[post_dict['creative']]
    print(2)
    new_vector[2] =  outdoors[post_dict['outdoors']]
    print(3)
    new_vector[3] =  career[post_dict['career']]
    print(4)
    new_vector[4] =  group_work[post_dict['group_work']]
    print(5)
    new_vector[5] =  liked_courses[post_dict['liked_courses']]
    print(6)
    new_vector[6] =  disliked_courses[post_dict['disliked_courses']]
    print(7)
    new_vector[7] =  programming[post_dict['programming']]
    print(8)
    new_vector[8] =  join_clubs[post_dict['join_clubs']]
    print(9)
    new_vector[9] =  not_clubs[post_dict['not_clubs']]
    print(10)
    new_vector[10] = liked_projects[post_dict['liked_projects']]
    print(11)
    new_vector[11] = disliked_projects[post_dict['disliked_projects']]
    print(12)
    new_vector[12] = tv_shows[post_dict['tv_shows']]
    print(13)
    new_vector[13] = alternate_degree[post_dict['alternate_degree']]
    print(14)
    new_vector[14] = expensive_equipment[post_dict['expensive_equipment']]
    print(15)
    new_vector[15] = drawing[post_dict['drawing']]
    print(16)
    new_vector[16] = essay[post_dict['essay']]
    print(17)
    new_vector[17] = architecture[post_dict['architecture']]
    print(18)
    new_vector[18] = automotive[post_dict['automotive']]
    print(19)
    new_vector[19] = business[post_dict['business']]
    print(20)
    new_vector[20] = construction[post_dict['construction']]
    print(21)
    new_vector[21] = health[post_dict['health']]
    print(22)
    new_vector[22] = environment[post_dict['environment']]
    print(23)
    new_vector[23] = manufacturing[post_dict['manufacturing']]
    print(24)
    new_vector[24] = technology[post_dict['technology']]
    print(25)
    print(post_dict)

    print("Loading model")
    pkl_file = open('poc/quiz/exported_model_files/'+model_name+'.pkl', 'rb')
    model = pickle.load(pkl_file)

    prediction = model.predict_proba([new_vector])
    print("Prediction created...")

    print("Creating new record...")
    print(post_dict)
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
