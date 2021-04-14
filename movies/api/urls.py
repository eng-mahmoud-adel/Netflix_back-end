from django.urls import path ,re_path
from . import views

urlpatterns=[
    path('',views.index),
    path('<int:pk>',views.edit),
    re_path('search', views.moviesList.as_view()),
    ]