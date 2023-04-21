from django.http import HttpResponse
from django.shortcuts import render
from base.models import Blog,Flaticon,Item,Chef

def home(request):
    menu_items = Item.objects.all()
    blogs = Blog.objects.all()
    flaticon = Flaticon.objects.all()
    context = {
        "items":menu_items,
        "blogs":blogs,
        "flaticons":flaticon, 
        }
    return render(request, "index.html", context)
def menu(request):
    flaticon = Flaticon.objects.all()

    menu_items = Item.objects.all()
    context = {
        "items":menu_items,
        "flaticons":flaticon
        }
    return render(request, "menu.html", context)
def services(request):
    flaticon = Flaticon.objects.all()
    menu_items = Item.objects.all()
    context = {"flaticons":flaticon, "items":menu_items}
    return render(request, "services.html", context)
def blog(request):
    return render(request, "blog.html")
def about(request):
    chef = Chef.objects.all()
    flaticon = Flaticon.objects.all()
    context = {"chefs":chef, "flaticons":flaticon}
    return render(request, "about.html", context)
def contact(request):
    return render(request, "contact.html")


#   path("", views.home, name ="home"),
#     path("menu", views.menu, name ="menu")
#     path("services", views.services, name ="services")
#     path("blog", views.blog, name ="blog")
#     path("about", views.about, name ="about")
#     path("contact", views.contact, name ="contact")'