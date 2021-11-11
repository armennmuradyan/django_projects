from django.urls import path
from to_do import views

urlpatterns = [
    path('', views.home),
    path('greeting/', views.greeting),
    path('intro/', views.introduction),
    path('dt/', views.date_time),
    path('task/', views.task),
]