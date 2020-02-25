from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
from core.models import *

class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program
        fields = ('id', 'name', 'code',)

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        fields = ('id', 'program', 'course',)

class ResultResource(resources.ModelResource):
    class Meta:
        model = Result
        fields = ('id', 'email', 'problem_type','creative','outdoors','career','group_work','liked_courses','disliked_courses','programming','join_clubs','not_clubs','liked_projects','disliked_projects','tv_shows','alternate_degree','expensive_equipment','drawing','essay',)

class ProgramAdmin(ImportExportModelAdmin):
    resource_class = ProgramResource

class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource

class ResultAdmin(ImportExportModelAdmin):
    resource_class = ResultResource

admin.site.register(Program, ProgramAdmin)
admin.site.register(Description)
admin.site.register(Comparison)
admin.site.register(Career)
admin.site.register(Course, CourseAdmin)
admin.site.register(Result, ResultAdmin)
