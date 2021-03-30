
from django.urls import path, re_path
from . import views

urlpatterns= [
    path("",views.index),
    path("create",CreateSeries.as_view()),
    path("delete/<int:pk>", views.delete),
    path("update/<int:id>",views.update),
    re_path('search', views.SeriesList.as_view()),
]