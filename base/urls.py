from django.urls import path 
from . import views


urlpatterns = [

    path("loginForm/",views.loginForm,name="loginForm"),
    path("registerForm/",views.registerForm,name="registerForm"),
    path("logoutForm/",views.logoutForm,name="logoutForm"),
    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("address/",views.address,name="address"),
    path("", views.home, name ="home"),
    path("menu/", views.menu, name ="menu"),
    path("services/", views.services, name ="services"),
    path("blog/", views.blog, name ="blog"),
    path("about/", views.about, name ="about"),
    path("contact/", views.contact, name ="contact"),
    path("cart/", views.cart, name="cart"),
    path("blog/", views.cart, name="blog"),
    path("blog1/", views.cart, name="blog1"),
    #signup and order urls
] 
