from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name ='home'),
    path('about/', views.About, name ='About'),
    path('', views.login_person, name ='login'),
    path('logout/', views.logout_person,name = 'logout'),
    path('register/', views.registration,name = 'registration'),
    path('product/<int:pk>', views.product_view,name = 'product'),




 

]