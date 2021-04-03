from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

urlpatterns=[
     path("login/", obtain_auth_token),
     path("logout/", views.Logout.as_view()),
     path('signup/',views.api_signup),
     path('profiles/<int:user>',views.api_profiles),
     path('profile/<int:id>',views.api_profile),
     path('create/profile',views.create_profile),
     path('up_del/profile/<int:id>',views.up_del_profile),
    
]