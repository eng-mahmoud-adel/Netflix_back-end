
from django.urls import path, re_path
from . import views

urlpatterns= [
    path("",views.index),
    path("create",views.create),
    path("delete/<int:pk>",views.DeleteSeries.as_view()),
    path("update/<int:id>",views.update),
    re_path('search', views.SeriesList.as_view()),
    path("<int:pk>", views.RetrieveSeries.as_view()),

]