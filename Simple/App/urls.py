from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('add_route/', views.add_route, name='add_route'),
    path('add_delivery/', views.add_delivery, name='add_delivery'),
    path('add_booking/', views.add_booking, name='add_booking'),
]