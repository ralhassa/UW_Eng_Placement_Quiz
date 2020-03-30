from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

# Defining Resources
class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program
        fields = ('id', 'name',)

class EmailResource(resources.ModelResource):
    class Meta:
        model = Email
        fields = ('id', 'email',)

class DescriptionResource(resources.ModelResource):
    class Meta:
        model = Description
        fields = ('id','program','description','hyperlink',)

class CareerTypeResource(resources.ModelResource):
    class Meta:
        model = CareerType
        fields = ('id','option',)

class CourseTypeResource(resources.ModelResource):
    class Meta:
        model = CourseType
        fields = ('id','option',)

class CareerResource(resources.ModelResource):
    class Meta:
        model = Career
        fields = ('id','program','career_type','career',)

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        fields = ('id', 'program','course_type','course',)

class RecommendationResource(resources.ModelResource):
    class Meta:
        model = Recommendation
        fields = ('id', 'program','description','code',)

class ComparisonResource(resources.ModelResource):
    class Meta:
        model = Comparison
        fields = ('id','program_1','program_2','comparison','recommendation',)

class ResultResource(resources.ModelResource):
    class Meta:
        model = Result
        fields = ('id', 'time', 'problem_type','creative','outdoors','career','group_work','liked_courses','disliked_courses','programming','join_clubs','not_clubs','liked_projects','disliked_projects','tv_shows','alternate_degree','expensive_equipment','drawing','essay','arch','arche','bmed','ce','cive','chem','env','elec','geo','mech','msci','nano','syde','swe','tron',)




# Defining Admin Objects
class ProgramAdmin(ImportExportModelAdmin):
    resource_class = ProgramResource

class EmailAdmin(ImportExportModelAdmin):
    resource_class = EmailResource

class DescriptionAdmin(ImportExportModelAdmin):
    resource_class = DescriptionResource

class CareerTypeAdmin(ImportExportModelAdmin):
    resource_class = CareerTypeResource

class CourseTypeAdmin(ImportExportModelAdmin):
    resource_class = CourseTypeResource

class CareerAdmin(ImportExportModelAdmin):
    resource_class = CareerResource

class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource

class RecommendationAdmin(ImportExportModelAdmin):
    resource_class = RecommendationResource

class ComparisonAdmin(ImportExportModelAdmin):
    resource_class = ComparisonResource

class ResultAdmin(ImportExportModelAdmin):
    resource_class = ResultResource

# Registering on Admin Site
admin.site.register(Program, ProgramAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(CareerType, CareerTypeAdmin)
admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(Comparison, ComparisonAdmin)
admin.site.register(Result, ResultAdmin)
