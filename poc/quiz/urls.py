from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('form', views.form, name='form'),
    path('download_to_csv',views.download_to_csv,name='download_to_csv'),
    url(r'submit', views.submit, name='submit'),
]
