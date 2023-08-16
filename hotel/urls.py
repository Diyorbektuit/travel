from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.hotel_list, name="hotels"),
    path('hotels/<int:pk>/', views.hotel_detail, name="hotel"),
    path('basket_hotel/<int:pk>/', views.hotel_booking, name="booking"),

]
