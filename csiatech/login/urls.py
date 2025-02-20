from django.urls import path
from . import views

urlpatterns = [path("", views.custom_login, name="login")]

# urlpatterns = [
#     path("", views.login, name="login")
#     path('login/', login_view, name='login'),
#     # Add other login-related paths as needed
# ]