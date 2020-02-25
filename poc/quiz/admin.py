from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class ViewResult(ImportExportModelAdmin):
    pass

class ViewProgram(ImportExportModelAdmin):
    pass

class ViewDescription(ImportExportModelAdmin):
    pass

class ViewComparison(ImportExportModelAdmin):
    pass

class ViewCourse(ImportExportModelAdmin):
    pass

class ViewCareer(ImportExportModelAdmin):
    pass

admin.site.register(Course)
admin.site.register(Career)
admin.site.register(Comparison)
admin.site.register(Description)
admin.site.register(Result)
admin.site.register(Program)
