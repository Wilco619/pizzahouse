from django.urls import path 
from . import views


urlpatterns = [
    path("", views.home, name ="home"),
    path("menu", views.menu, name ="menu"),
    path("services", views.services, name ="services"),
    path("blog", views.blog, name ="blog"),
    path("about", views.about, name ="about"),
    path("contact", views.contact, name ="contact"),
    path("cart", views.cart, name="cart"),
    #signup and order urls
    path("order", views.order, name ="order"),
    path("signup",views.signup,name="signup"),
    path("add_to_order/<int:itemId>", views.add_to_order, name="add_to_order"),
] 
