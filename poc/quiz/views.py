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
            return response(request,post_dict)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return HttpResponse("Something went wrong...create) 3")

def response(request,post_dict):
    '''
    I copied the encoded dictionary over because it was taking too long to figure out how to read it

    I also moved the nb_model.pkl file and the cat file over from model building into the quiz folders
    '''
    print("Entered Response Creation...")
    encoded_dictionary = [{"Rainy": 1, "Overcast": 0, "Sunny": 2, "column": "OUTLOOK"}, {"Hot": 1, "Mild": 2, "Cool": 0, "column": "TEMPERATURE"}, {"High": 0, "Normal": 1, "column": "HUMIDITY"}, {"FALSE": 0, "TRUE": 1, "column": "WINDY"}, {"No": 0, "Yes": 1, "column": "PLAY"}]

    outlook = encoded_dictionary[0]
    temperature = encoded_dictionary[1]
    humidity = encoded_dictionary[2]
    windy = encoded_dictionary[3]

	#Prepare the feature vector for prediction

    print("Loading new_vector....")
    pkl_file = open('quiz/cat', 'rb')
    index_dict = pickle.load(pkl_file)
    new_vector = np.zeros(len(index_dict))

    print("Loading response into new_vector...")
    new_vector[0] = outlook[post_dict['OUTLOOK']]
    new_vector[1] = temperature[post_dict['TEMPERATURE']]
    new_vector[2] = humidity[post_dict['HUMIDITY']]
    new_vector[3] = windy[post_dict['WINDY']]
    print(post_dict)

    print("Loading model")
    pkl_file = open('quiz/nb_model.pkl', 'rb')
    nb_model = pickle.load(pkl_file)
    prediction = nb_model.predict([new_vector])
    response_message = ''
    if prediction == 0:
        response_message  = 'You should not play golf today'
        rm = 'NO'
    else:
        response_message = 'You could play golf today'
        rm = 'YES'

    print("Prediction created...")

    print("Creating new record...")
    print(post_dict)
    new_record = Results()
    new_record.name = post_dict['name']
    new_record.email = post_dict['email']
    new_record.OUTLOOK = post_dict['OUTLOOK']
    new_record.TEMPERATURE = post_dict['TEMPERATURE']
    new_record.HUMIDITY = post_dict['HUMIDITY']
    new_record.WINDY = post_dict['WINDY']
    new_record.PLAY = rm
    new_record.save()

    context = {
        'response_message':response_message,
        'new_record':str(new_record)
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
