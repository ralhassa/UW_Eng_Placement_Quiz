from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import sys

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
            return render(request, 'quiz/response.html')
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return HttpResponse("Something went wrong...create) 3")
