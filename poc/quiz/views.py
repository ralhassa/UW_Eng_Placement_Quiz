import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import json
import pickle
import numpy as np
import sys

from . models import *

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

def response(request,post_dict,model_name):
    print("Entered Response Creation...")
    encoded_dictionary = get_encoded_dict(model_name)

    program = encoded_dictionary['program']
    problem_type = encoded_dictionary['problem_type']
    creative = encoded_dictionary['creative']
    outdoors = encoded_dictionary['outdoors']
    career = encoded_dictionary['career']
    group_work = encoded_dictionary['group_work']
    liked_courses = encoded_dictionary['liked_courses']
    disliked_courses = encoded_dictionary['disliked_courses']
    programming = encoded_dictionary['programming']
    join_clubs = encoded_dictionary['join_clubs']
    not_clubs = encoded_dictionary['not_clubs']
    liked_projects = encoded_dictionary['liked_projects']
    disliked_projects = encoded_dictionary['disliked_projects']
    tv_shows = encoded_dictionary['tv_shows']
    alternate_degree = encoded_dictionary['alternate_degree']
    expensive_equipment = encoded_dictionary['expensive_equipment']
    drawing = encoded_dictionary['drawing']
    essay = encoded_dictionary['essay']
    architecture = encoded_dictionary['architecture']
    automotive = encoded_dictionary['automotive']
    business = encoded_dictionary['business']
    construction = encoded_dictionary['construction']
    health = encoded_dictionary['health']
    environment = encoded_dictionary['environment']
    manufacturing = encoded_dictionary['manufacturing']
    technology = encoded_dictionary['technology']

	# Prepare the feature vector for prediction

    print("Loading new_vector....")
    pkl_file = open('exported_model_files/'+model_name+'_cat', 'rb')
    index_dict = pickle.load(pkl_file)
    new_vector = np.zeros(len(index_dict))

    print("Loading response into new_vector...")
    new_vector[0] =  problem_type[post_dict['problem_type']]
    new_vector[1] =  creative[post_dict['creative']]
    new_vector[2] =  outdoors[post_dict['outdoors']]
    new_vector[3] =  career[post_dict['career']]
    new_vector[4] =  group_work[post_dict['group_work']]
    new_vector[5] =  liked_courses[post_dict['liked_courses']]
    new_vector[6] =  disliked_courses[post_dict['disliked_courses']]
    new_vector[7] =  programming[post_dict['programming']]
    new_vector[8] =  join_clubs[post_dict['join_clubs']]
    new_vector[9] =  not_clubs[post_dict['not_clubs']]
    new_vector[10] = liked_projects[post_dict['liked_projects']]
    new_vector[11] = disliked_projects[post_dict['disliked_projects']]
    new_vector[12] = tv_shows[post_dict['tv_shows']]
    new_vector[13] = alternate_degree[post_dict['alternate_degree']]
    new_vector[14] = expensive_equipment[post_dict['expensive_equipment']]
    new_vector[15] = drawing[post_dict['drawing']]
    new_vector[16] = essay[post_dict['essay']]
    new_vector[17] = architecture[post_dict['architecture']]
    new_vector[18] = automotive[post_dict['automotive']]
    new_vector[19] = business[post_dict['business']]
    new_vector[20] = construction[post_dict['construction']]
    new_vector[21] = health[post_dict['health']]
    new_vector[22] = environment[post_dict['environment']]
    new_vector[23] = manufacturing[post_dict['manufacturing']]
    new_vector[24] = technology[post_dict['technology']]
    print(post_dict)

    print("Loading model")
    pkl_file = open('exported_model_files/'+model_name+'.pkl', 'rb')
    nb_model = pickle.load(pkl_file)

    prediction = nb_model.predict_proba([new_vector])
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
        'response_message':str(prediction),
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
