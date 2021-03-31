from django.urls import path, re_path
from . import views

urlpatterns= [
    path("",views.index),
    path("create",views.create),
    path("update/<int:pk>",views.update),
    path("delete/<int:pk>",views.delete),
    path("<int:pk>", views.RetrieveEpisode.as_view()),


]