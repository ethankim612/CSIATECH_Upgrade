from django.urls import path
from club import views

urlpatterns = [
    path("club/", views.club_view, name="club"),
    # path("teacher_login/", views.teacher_login, name="teacher_login"),
    # Add other app1-related paths as needed
]