from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from crud.models import ClassRoom
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import ClassRoomForm, ClassRoomModelForm



# Create your views here.


class HomeView(TemplateView):
    template_name = "classbased/home.html"

    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        context["name"] = "Suraj"
        print(context)
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# class ClassRoomView(ListView):
#     queryset = ClassRoom.objects.all()
#     template_name = "classbased/classroom.html"
#     context_object_name = "classrooms"


#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         # form = ClassRoomForm()
#         form = ClassRoomModelForm()
#         context["form"] = form
        # return context

    # def post(self, *args, **kwargs):
    #     form = ClassRoomModelForm(self.request.POST)    # we are validating user input data
    #     if form.is_valid():
    #         print(form.cleaned_data)  # form.cleaned is a dict type
    #         # name = form.cleaned_data["name"]
    #         # ClassRoom.objects.create(name=name)
    #         form.save()
    #         messages.success(self.request, "Classroom added successfully")
    #     else:
    #         messages.error(self.request, "invalid form data")
    #     return redirect("classbased:classroom")      

class ClassroomListCreateView(CreateView):
    queryset = ClassRoom.objects.all()      #querysets are lazy in django
    template_name = "classbased/classroom.html"
    context_object_name = "classrooms"
    form_class = ClassRoomModelForm
    success_url = reverse_lazy("classbased:classroom")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classrooms"] = self.get_queryset()
        return context


    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            messages.success(request, "Classroom added successfully")
            return self.form_valid(form)
        else:
            messages.error(request, "Something went wrong !")
            return self.form_invalid(form)

class ClassroomUpdateView(UpdateView):
    queryset = ClassRoom.objects.all()
    template_name = "classbased/classroom_update.html"
    form_class = ClassRoomModelForm
    context_object_name = "classroom"
    success_url = reverse_lazy("classbased:classroom")

class ClassroomDeleteView(DeleteView):
    queryset = ClassRoom.objects.all()
    template_name = "classbased/classroom_delete.html"
    success_url = reverse_lazy("classbased:classroom")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            messages.success(request, "Classroom deleted successfully")
            return self.form_valid(form)
        else:
            messages.error(request, "Something went wrong !")
            return self.form_invalid(form)


        
        
      


