from django.urls import path, include
from . import views

urlpatterns=[
     # logout
     path("auth/logout/", views.Logout.as_view()),
     # login
     path('auth/', include('rest_auth.urls')),
     # signup
     path('auth/register/', include('rest_auth.registration.urls')), 
]