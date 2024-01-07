from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('profile', views.profile_view, name='profile'),
    path('login', views.login, name='login')
]
