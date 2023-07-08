from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body = models.TextField()
    blogId = models.IntegerField()
    author = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='static/images')
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
    


#cart class
# class Cart(models.Model):
#     purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.purchaser

#product class
class Product(models.Model):
    PIZZA = 'pizza'
    DRINK = 'drink'
    BURGER = 'burger'
    PASTA = 'pasta'

    CATEGORY_CHOICES = [
        (PIZZA, 'pizza'),
        (DRINK, 'drink'),
        (BURGER, 'burger'),
        (PASTA, 'pasta'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    composition = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    on_offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/images')
    def __str__(self):
        return self.title
    

class Customer(models.Model):
    NRB= 'nairobi'
    MO = 'mombasa'
    NAK = 'nakuru'
    KIS = 'kisumu'

    COUNTY_CHOICES = [
        (NRB, 'nairobi'),
        (MO, 'mombasa'),
        (NAK, 'nakuru'),
        (KIS, 'kisumu'),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    county = models.CharField(choices=COUNTY_CHOICES,max_length=200)
    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(null=True, blank=True)
    productId = models.ForeignKey(Product,on_delete=models.CASCADE)
    # Add any other fields as needed
    def __str__(self):
        return f"Order {self.productId} by {self.user.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    # Add any other fields as needed
    def __str__(self):
        return f"OrderItem {self.productId} of {self.quantity} {self.product.name} in Order {self.order.is_ordered}"
