from django.contrib import admin
from .models import Provider, Speciality, Availabilities

# Register your models here.
admin.site.register(Provider)
admin.site.register(Speciality)
admin.site.register(Availabilities)