from django.urls import path, include
from . import views

urlpatterns = [
    path('firstLogin/', views.firstLayerAuthentication),
    path('actualLogin/', views.LoginUser),
    path('', views.phoneLayer),
    path('dashboard/', views.dashboard)
]
