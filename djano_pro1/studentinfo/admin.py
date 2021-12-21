from django.contrib import admin
from .models import StudentInfo

class studentAdmin(admin.ModelAdmin):
    list_instances = ('name','roll_number','gender','father_name')

admin.site.register(StudentInfo,studentAdmin)



# Register your models here.
