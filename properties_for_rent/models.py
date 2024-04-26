from django.db import models
from django.utils import timezone

class Listing(models.Model):
    title = models.CharField(max_length=100)
    Rooms_available = models.IntegerField()
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    square_footage = models.IntegerField()
    AvailableBy = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100)
    # images = models.images()  # Not sure what you meant here, might need correction.

    def __str__(self):
        return self.title
