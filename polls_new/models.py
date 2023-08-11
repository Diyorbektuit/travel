from django.contrib.auth.models import User
from django.db import models

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