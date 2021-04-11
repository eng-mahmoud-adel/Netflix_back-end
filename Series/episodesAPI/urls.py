from django.urls import path, re_path
from . import views

urlpatterns= [
    path("",views.index),
    path("create",views.create),
    path("update/<int:pk>",views.update),
    path("delete/<int:pk>",views.DeleteEpisode.as_view()),
    path("<int:pk>", views.RetrieveEpisode.as_view()),
    re_path('search', views.episodesList.as_view()),

]