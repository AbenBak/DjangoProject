from django.contrib import admin
from .models import Airports,Planes,Flight,Travelers
admin.register([Airports,Planes,Flight,Travelers])
# Register your models here.
