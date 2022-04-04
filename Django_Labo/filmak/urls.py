from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('menua', views.menua, name='menua'),
    path('filmakIkusi', views.filmakIkusi, name='filmakIkusi'),
    path('bozkatu', views.bozkatu, name='bozkatu'),
    path('zaleak', views.zaleak, name='zaleak'),
    path('', views.logout, name='logout'),
]