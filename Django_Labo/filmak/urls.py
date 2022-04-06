from django.urls import path
from django.contrib.auth import logout as logout
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('menua/', views.menua, name='menua'),
    path('filmakIkusi/', views.filmakIkusi, name='filmakIkusi'),
    path('bozkatu/', views.bozkatu, name='bozkatu'),
    path('zaleak/', views.zaleak, name='zaleak'),
    path('logout/', views.logout, name='logout'),
    #path(r'^logout', logout({'next_name ' : '/'}), name='logout'),
    #path('logout/', LogoutView.as_view(), name="logout")
]