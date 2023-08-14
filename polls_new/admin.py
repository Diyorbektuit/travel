from django.contrib import admin
from .models import TouristPlace, PaymentItem, PaymentItemAdmin, TouristPlaceAdmin

admin.site.register(TouristPlace, TouristPlaceAdmin)
admin.site.register(PaymentItem, PaymentItemAdmin)