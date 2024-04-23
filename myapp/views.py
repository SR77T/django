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
