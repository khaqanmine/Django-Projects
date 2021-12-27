from django.contrib import admin
from contactform.models import ContactFormModel

class ContactFormModelAdmin(admin.ModelAdmin):
    list_instances = ('name', 'phone', 'email')

admin.site.register(ContactFormModel, ContactFormModelAdmin)
# Register your models here.
