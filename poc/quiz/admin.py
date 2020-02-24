from django.contrib import admin
from import_export.admin import ImportExportModeladmin
from .models import *

admin.site.register(Result)
# class ViewResult(ImportExportModelAdmin):
#     pass
admin.site.register(Program)
# class ViewProgram(ImportExportModelAdmin):
#     pass
admin.site.register(Description)
# class ViewDescription(ImportExportModelAdmin):
#     pass
admin.site.register(Comparison)
# class ViewComparison(ImportExportModelAdmin):
#     pass
admin.site.register(Course)
# class ViewCourse(ImportExportModelAdmin):
#     pass
admin.site.register(Career)
# class ViewCareer(ImportExportModelAdmin):
#     pass
