from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>', views.room, name='room'),
    path('user_register/', views.User_register, name="user_registration"),
    path('login/', views.Login, name="login")
]  