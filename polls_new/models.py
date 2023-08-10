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


