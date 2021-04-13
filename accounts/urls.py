from django.urls import path, include
from . import views

urlpatterns=[
     # logout
     path("auth/logout/", views.Logout.as_view()),
     # login
     path('auth/', include('rest_auth.urls')),
     # signup
     path('auth/register/', include('rest_auth.registration.urls')),
     path('auth/google/', views.GoogleLogin.as_view(), name='google_login'),
     # profiles
     path('profiles/',views.profiles),
     path('profile/<int:id>',views.profile),
     path('create_profile',views.create_profile),
     path('update_delete_profile/<int:id>',views.update_delete_profile),
]