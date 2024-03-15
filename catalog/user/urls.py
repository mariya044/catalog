from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns=[
    path('signup/',views.SignUp.as_view(),name="signup"),

]