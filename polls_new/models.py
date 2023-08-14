from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

# Create your models here.


class TouristPlace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='tourist_places/', blank=True, null=True)

    def __str__(self):
        return self.name


class PaymentItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(TouristPlace, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

                                                                                    #for payment
    def __str__(self):
        return f"{self.user.username}'s PaymentItem: {self.item.name}"


class TouristPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price')
    list_filter = ('location',)
    search_fields = ('name', 'location')

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.something_specific:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.something_specific:
            return False
        return True


class PaymentItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity')
    list_filter = ('user',)
    search_fields = ('user__username', 'item__name')

    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and request.user.is_superuser:
            return False
        return True


