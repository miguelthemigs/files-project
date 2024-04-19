from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('profile/<str:pk>/', views.userProfile, name="profile"),
    
    path('feedback/', views.userProfile, name="profile"),


    path('randomize/', views.show_doc, {'randomize': 1}, name='show-doc-randomize'),  # URL to fetch a random document
    path('<str:doc_id>/', views.show_doc, name='show-doc'),
    path('<str:doc_id>/<int:page_number>/', views.show_doc, name='show-doc-page'),
]
