from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views


app_name = "api"

router = DefaultRouter()

router.register("viewset/classroom", views.ClassRoomViewSet, basename = "classroom")
router.register("viewset/student", views.StudentViewSet, basename = "student")



urlpatterns = [
    path("student/", views.StudentView.as_view(), name = "student"),
    path("student/<int:id>/", views.StudentDetailView.as_view(), name = "student_detail"),
    path("classroom/", views.ClassRoomView.as_view(), name = "classroom"),
    path("classroom/<int:id>/", views.ClassRoomView.as_view(), name = "classroom_patch"),
    path("login/", obtain_auth_token )


 
] + router.urls

using_serializer_path= [
    path('classroom-using-serializer/<int:id>/', views.ClassRoomUsingSerializerDetailView.as_view()),
    path('using-serializer/classroom/', views.ClassRoomListUsingSerializerView.as_view()),
    path('using-serializer/student/', views.StudentUsingSerializerView.as_view()),


]
using_model_serializer_paths = [
    path("using-model-serializer/student/", views.StudentUsingModelSerView.as_view())
]

generic_urls = [
    path("generic/classroom-list/", views.ClassRoomGenericListView.as_view()),
    path("generic/classroom-create/", views.ClassRoomGenericCreateView.as_view()),
    path("generic/classroom/", views.ClassRoomGenericView.as_view()),
    path("generic/classroom-update/<int:pk>/", views.ClassRoomGenericUpdateView.as_view()),
    path("generic/classroom-detail/<int:pk>/", views.ClassRoomGenericDetailView.as_view()),
    path("generic/classroom-delete/<int:pk>/", views.ClassRoomGenericDeleteView.as_view()),
    path("generic/student/", views.StudentGenericView.as_view()),
    path("generic/student/detail-delete-update/<int:pk>/", views.StudentRetrieveUpdateDestroyGenericView.as_view()),








]

urlpatterns += using_serializer_path + using_model_serializer_paths + generic_urls