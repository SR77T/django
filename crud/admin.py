from django.contrib import admin
from .models import Student

# Register your models here.
admin.site.register(Student)

# Student.objects.all() # [obj1, obj2, ....]