from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('recommendations', views.recommendations, name='recommendations'),
    path('download_to_csv',views.download_to_csv,name='download_to_csv'),
    url(r'submit', views.submit, name='submit'),
]
