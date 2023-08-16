from django.shortcuts import render
from .models import Hotel
from django.contrib import messages
from django.shortcuts import render


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels_list.html', {'hotels': hotels})


def hotel_detail(request, pk):
    hotel = Hotel.objects.get(id=pk)
    contex = {'hotel': hotel}
    return render(request, 'hotel_detail.html', contex)


def hotel_booking(request, pk):
    booking = Hotel.objects.get(id=pk)
    contex = {'booking': booking}
    return render(request, 'basket_hotel.html', contex)








