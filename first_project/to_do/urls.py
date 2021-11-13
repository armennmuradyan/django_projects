from django.urls import path
from to_do import views

urlpatterns = [
    path('', views.home),
    path('newurl/', views.new_url),
    path("filtered_data/",views.filtered_data)
]