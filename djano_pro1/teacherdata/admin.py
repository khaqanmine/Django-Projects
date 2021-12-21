from django.contrib import admin
from teacherdata.models import TeacherData


# Table will be show on admin side

class TeacherDataAdmin(admin.ModelAdmin):
    list_instances = ('name','phone','address','salary')

admin.site.register(TeacherData,TeacherDataAdmin)

# Register your models here.
