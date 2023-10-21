from django.contrib import admin
from django.urls import path,include
from Restaurant_App import views

urlpatterns = [
    path('', views.index,name="Home"),
    path('contact/', views.contact,name="Contact"),
    path('menu/', views.menu,name="Menu"),
    path('qc_food_order/', views.qrcode,name="qrcode")
    # path('about/', views.about,name="About"),
    # path('services/', views.services,name="Services"),
   
]