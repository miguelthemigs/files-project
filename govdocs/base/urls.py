from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('dashboard/', views.inputlog_dashboard, name="inputlog_dashboard"),

    path('profile/<str:pk>/', views.userProfile, name="profile"),

    #path('input/<str:doc_id>/<int:input_type>/', views.inputForm, name='inputform'),
    path('randomize/', views.show_doc, {'randomize': 1}, name='show-doc-randomize'),  # URL to fetch a random document
    path('<str:doc_id>/', views.show_doc, name='show-doc'),
    path('<str:doc_id>/<int:page_number>/', views.show_doc, name='show-doc-page'),
    
    path('<str:doc_id>/<int:page_number>/<int:input_type>/<int:avaliar>/', views.show_doc, name='show-doc-input-type'),

    path('<str:doc_id>/<int:page_number>/<int:input_type>/<int:avaliar>/<int:input_id>/', views.show_doc, name='show-doc-avaliar'),
    
    path('increase_points/<int:input_id>', views.increaseInputPoint, name='increase-points'),
    path('decrease_points/<int:input_id>', views.decreaseInputPoint, name='decrease-points'),
    
    
]
