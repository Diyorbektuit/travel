from django.contrib.auth.models import User
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    cost = models.CharField(max_length=10)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


#class HotelBooking(models.Model):






#class HotelReview(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#    stars = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
#    review_text = models.TextField()
#
#    def __str__(self):
#        return f"{self.user.username} - {self.hotel.name} ({self.stars} stars)"
#
#