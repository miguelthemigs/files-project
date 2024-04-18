from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="header"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),

    path('document/<str:doc_id>/', views.show_doc, name='show-doc'),

]
