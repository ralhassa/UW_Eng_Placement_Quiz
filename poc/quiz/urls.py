from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    url(r'submit', views.submit, name='submit'),
]
