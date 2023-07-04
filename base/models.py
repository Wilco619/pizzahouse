from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    main_image = models.ImageField(upload_to='static/images')
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    blogId = models.IntegerField()
    author = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
class Flaticon(models.Model):
    icon= models.ImageField(upload_to='static/images')
    title= models.CharField(max_length=255)
    description= models.TextField()
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class Chef(models.Model):
    image = models.ImageField(upload_to='static/images')
    name= models.CharField(max_length=255)
    position= models.CharField(max_length=255)
    description= models.TextField()
    def __str__(self):
        return self.name
    

# order and order item models
class Item(models.Model):
    image = models.ImageField(upload_to='static/images')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    itemId = models.IntegerField()
    category = models.CharField(max_length=255)
    onOffer =models.BooleanField(default=False)
    def __str__(self):
        return self.name
# date = auto_now_add =True

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(null=True, blank=True)
    itemId = models.ForeignKey(Item,on_delete=models.CASCADE)
    # Add any other fields as needed
    def __str__(self):
        return f"Order {self.itemId} by {self.user.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    itemId = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    # Add any other fields as needed
    def __str__(self):
        return f"OrderItem {self.itemId} of {self.quantity} {self.item.name} in Order {self.order.is_ordered}"
