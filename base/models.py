from django.db import models

from django.db import models

class Item(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    itemId = models.IntegerField()
    cat = models.CharField(max_length=255)
    onOffer =models.BooleanField(default=False)
    def __str__(self):
        return self.name
# date = auto_now_add =True
from django.db import models
class Blog(models.Model):
    main_image = models.CharField(max_length=255)
    other_images = models.TextField()
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    blogId = models.IntegerField()
    author = models.CharField(max_length=255)
    def __str__(self):
        return self.title
class Flaticon(models.Model):
    icon= models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    description= models.TextField()
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type
class Chef(models.Model):
    image = models.CharField(max_length=255)
    name= models.CharField(max_length=255)
    position= models.CharField(max_length=255)
    description= models.TextField()
    def __str__(self):
        return self.name