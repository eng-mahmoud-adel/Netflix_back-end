from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
     path("login/", obtain_auth_token),
     path("logout/", views.Logout.as_view(), name='logout'),
     # path('api/login',obtain_auth_token)
]