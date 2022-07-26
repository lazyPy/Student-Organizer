from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.homePage, name='home'),
    path('topic/<str:pk>/', views.topic, name='topic'),
    path('create-topic/', views.createTopic, name='create-topic'),
    path('profile/<str:pk>/', views.profile, name='profile')
]