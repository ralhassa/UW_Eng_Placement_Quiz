from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program
        fields = ('id', 'name', 'code',)

class DescriptionResource(resources.ModelResource):
    class Meta:
        model = Description
        fields = ('id','program','description',)

class ComparisonResource(resources.ModelResource):
    class Meta:
        model = Comparison
        fields = ('id','program1','program_2','comparison',)

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        fields = ('id', 'program', 'course',)

class CareerResource(resources.ModelResource):
    class Meta:
        model = Career
        fields = ('id','program','career',)

class ResultResource(resources.ModelResource):
    class Meta:
        model = Result
        fields = ('id', 'email', 'problem_type','creative','outdoors','career','group_work','liked_courses','disliked_courses','programming','join_clubs','not_clubs','liked_projects','disliked_projects','tv_shows','alternate_degree','expensive_equipment','drawing','essay',)

class ProgramAdmin(ImportExportModelAdmin):
    resource_class = ProgramResource

class DescriptionAdmin(ImportExportModelAdmin):
    resource_class = DescriptionResource

class ComparisonAdmin(ImportExportModelAdmin):
    resource_class = ComparisonResource

class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource

class CareerAdmin(ImportExportModelAdmin):
    resource_class = CareerResource

class ResultAdmin(ImportExportModelAdmin):
    resource_class = ResultResource

admin.site.register(Program, ProgramAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Comparison, ComparisonAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Result, ResultAdmin)
