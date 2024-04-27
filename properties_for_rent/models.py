from django.db import models
from django.utils import timezone
from os import listdir
import os.path
from os.path import isfile
from os.path import join as path_join
from random import choice

class Listing(models.Model):
    title = models.CharField(max_length=100)
    Rooms_available = models.IntegerField()
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    square_footage = models.IntegerField()
    AvailableBy = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100)
    image = models.ImageField()
    # images = models.images()  # Not sure what you meant here, might need correction.

    def __str__(self):
        return self.title
    # def random_img():
    #     dir_path = os.path.join(BASE_DIR, 'media')
    #     files = [
    #         content for content in listdir(dir_path)
    #         if isfile(path_join(dir_path, content))
    #     ]
    #     return choice(files)
