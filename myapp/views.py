from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    query_strings = request.GET
    name = query_strings.get("name")
    return HttpResponse(f"Hello world. I am {name}")

def home_detail(request, id):
    return HttpResponse(f"My home id is {id}")

def portfolio(request):
    return render(request, template_name="myapp/portfolio.html")

def root_page(request):
    return render(request, template_name="myapp/root_page.html")

def learning_context(request):
    student = {"name": "jon", "age": 30, "email": "jon@gmail.com", "address": "Ktm"}
    students = [
        {"name": "jon", "age": 30, "email": "jon@gmail.com", "address": "Ktm"},
        {"name": "jon", "age": 30, "email": "jon@gmail.com", "address": "Ktm"},
        {"name": "jon", "age": 30, "email": "jon@gmail.com", "address": "Ktm"},
        {"name": "jon", "age": 30, "email": "jon@gmail.com", "address": "Ktm"},

    ]
    # return render (request, template_name="myapp/learning_context.html", context = student)
    # student.update(students)
    return render (request, template_name="myapp/learning_context.html", context = {"students": students, "student": student})


def using_bootstrap(request):
    students = [
    {"name": "jon", "age": 30, "email": "jon@gmail.com", "address": "Ktm"},
    {"name": "Ram", "age": 20, "email": "ram@gmail.com", "address": "Pkr"},
    {"name": "Jane", "age": 25, "email": "jane@gmail.com", "address": "Btm"},
    {"name": "Hary", "age": 27, "email": "hary@gmail.com", "address": "Bdp"},

]
    return render(request, template_name = "myapp/using_bs.html", context = {"students": students})

