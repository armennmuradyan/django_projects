from django.urls import path

from new_app import views

urlpatterns = [
    path('home', views.home)
]