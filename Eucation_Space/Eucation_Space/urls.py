from django.contrib import admin
from django.urls import path, include
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
    path('my_app/', include('my_app.urls')),
    path('logout/', views.Logout, name="logout"),
    path('special/', views.special, name="special"),
]