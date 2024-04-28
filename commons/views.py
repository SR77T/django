from django.shortcuts import render
from crud.models import Student

# Create your views here.\\


def student(request):
#     students = [
#     {"name": "jon", "age": 30, "email": "jon@gmail.com", "address": "Ktm"},
#     {"name": "Ram", "age": 20, "email": "ram@gmail.com", "address": "Pkr"},
#     {"name": "Jane", "age": 25, "email": "jane@gmail.com", "address": "Btm"},
#     {"name": "Hary", "age": 27, "email": "hary@gmail.com", "address": "Bdp"},

# ]
    students = Student.objects.all()
    return render (request, template_name="commons/student.html", context = {"students" : students})

def classroom(request):
    classrooms = [
        {"name": "One", "section": "A"},
        {"name": "Two", "section": "A"},
        {"name": "Three", "section": "A"},
        {"name": "Four", "section": "A"},
        {"name": "Five", "section": "A"},
    ]
    return render(request, template_name = "commons/classroom.html", context = {"classrooms": classrooms})

