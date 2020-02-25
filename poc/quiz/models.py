from django.db import models
# 
# class Program(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     code = models.CharField(max_length=20)
#     def __str__(self):
#         return str(self.name)
#
# class Description(models.Model):
#     id = models.AutoField(primary_key=True)
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#     description = models.TextField()
#     def __str__(self):
#         return str(self.program)+" : "+str(self.description)
#
# class Comparison(models.Model):
#     id = models.AutoField(primary_key=True)
#     program_1 = models.ForeignKey(Program, on_delete=models.CASCADE,related_name='program+')
#     program_2 = models.ForeignKey(Program, on_delete=models.CASCADE,related_name='compared_to+')
#     comparison = models.TextField()
#     def __str__(self):
#         return str(self.program_1)+" vs. "+str(self.program_2)+" : "+str(self.comparison)
#
# class Course(models.Model):
#     id = models.AutoField(primary_key=True)
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#     course = models.CharField(max_length=200)
#     def __str__(self):
#         return str(self.program)+" : "+str(self.course)
#
# class Career(models.Model):
#     id = models.AutoField(primary_key=True)
#     program = models.ForeignKey(Program, on_delete=models.CASCADE)
#     career = models.CharField(max_length=200)
#     def __str__(self):
#         return str(self.program)+" : "+str(self.career)
#
# class Result(models.Model):
#     id = models.AutoField(primary_key=True)
#     email = models.CharField(max_length=200)
#     problem_type = models.CharField(max_length=200)
#     creative = models.CharField(max_length=200)
#     outdoors = models.CharField(max_length=200)
#     career = models.CharField(max_length=200)
#     group_work = models.CharField(max_length=200)
#     liked_courses = models.CharField(max_length=200)
#     disliked_courses = models.CharField(max_length=200)
#     programming = models.CharField(max_length=200)
#     join_clubs = models.CharField(max_length=200)
#     not_clubs = models.CharField(max_length=200)
#     liked_projects = models.CharField(max_length=200)
#     disliked_projects = models.CharField(max_length=200)
#     tv_shows = models.CharField(max_length=200)
#     alternate_degree = models.CharField(max_length=200)
#     expensive_equipment = models.CharField(max_length=200)
#     drawing = models.CharField(max_length=200)
#     essay = models.CharField(max_length=200)
#     architecture = models.CharField(max_length=200)
#     automotive = models.CharField(max_length=200)
#     business = models.CharField(max_length=200)
#     construction = models.CharField(max_length=200)
#     health = models.CharField(max_length=200)
#     environment = models.CharField(max_length=200)
#     manufacturing = models.CharField(max_length=200)
#     technology = models.CharField(max_length=200)
#
#     def __str__(self):
#         return_value = (
#                         str(self.problem_type) + " , " +
#                         str(self.creative) + " , " +
#                         str(self.outdoors) + " , " +
#                         str(self.career) + " , " +
#                         str(self.group_work) + " , " +
#                         str(self.liked_courses) + " , " +
#                         str(self.disliked_courses) + " , " +
#                         str(self.programming) + " , " +
#                         str(self.join_clubs) + " , " +
#                         str(self.not_clubs) + " , " +
#                         str(self.liked_projects) + " , " +
#                         str(self.disliked_projects) + " , " +
#                         str(self.tv_shows) + " , " +
#                         str(self.alternate_degree) + " , " +
#                         str(self.expensive_equipment) + " , " +
#                         str(self.drawing) + " , " +
#                         str(self.essay) + " , " +
#                         str(self.architecture) + " , " +
#                         str(self.automotive) + " , " +
#                         str(self.business) + " , " +
#                         str(self.construction) + " , " +
#                         str(self.health) + " , " +
#                         str(self.environment) + " , " +
#                         str(self.manufacturing) + " , " +
#                         str(self.technology)
#                         )
#         return return_value
