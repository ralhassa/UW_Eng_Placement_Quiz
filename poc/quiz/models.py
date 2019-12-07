from django.db import models

class Results(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)
    answer_5 = models.CharField(max_length=200)
    answer_6 = models.CharField(max_length=200)
    answer_7 = models.CharField(max_length=200)
    answer_8 = models.CharField(max_length=200)
    answer_9 = models.CharField(max_length=200)
    answer_10 = models.CharField(max_length=200)
