from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path("", home, name="home"),
    path("signup/", sign_up, name="sign_up"),
    path("login/", log_in, name="log_in"),
    path("logout/", log_out, name="log_out"),
]