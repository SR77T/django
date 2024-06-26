from django.urls import path
from . import views


app_name = "classsbased"


urlpatterns = [
    # path("classroom/", views.ClassRoomView.as_view(), name = "classroom" ),
    path("classroom/", views.ClassroomListCreateView.as_view(), name = "classroom" ),
    path("classroom-update/<int:pk>/", views.ClassroomUpdateView.as_view(), name = "classroom_update"),
    path("classroom-delete/<int:pk>/", views.ClassroomDeleteView.as_view(), name = "classroom_delete"),

    path("student/", views.StudentView.as_view(), name = "student"),
    path("student-create/", views.StudentCreateView.as_view(), name = "student_create"),
    path("student-delete/<int:pk>/", views.StudentDeleteView.as_view(), name = "student_delete"),
    path("student-detail/<int:pk>/", views.StudentDetailView.as_view(), name = "student_detail"),
    path("student-update/<int:pk>/", views.StudentUpdateView.as_view(), name = "student_update"),   

    



    path("", views.HomeView.as_view(), name = "home")
]