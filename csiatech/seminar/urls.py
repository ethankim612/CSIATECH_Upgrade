from django.urls import path
from seminar import views

urlpatterns = [path("seminar/", views.seminar_room_view, name="seminar")]