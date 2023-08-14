from django.shortcuts import render
from .models import Hotel
from django.contrib import messages


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels_list.html', {'hotels': hotels})


def hotel_detail(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    return render(request, 'hotel_detail.html', {hotel:'hotel'})






