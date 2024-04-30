from django.shortcuts import render, redirect
from .models import Student, ClassRoom

# Create your views here.

def student(request):
    students = Student.objects.all()
    return render(request, template_name="crud/student.html", context = {"students" : students})

def classroom(request):
    if request.method == "POST":
        classroom_name = request.POST.get("classroom_name")
        ClassRoom.objects.create(name = classroom_name)
        return redirect("crud_classroom")

    classrooms = ClassRoom.objects.all()
    return render(request, template_name="crud/classroom.html", context = {"classrooms" : classrooms})


