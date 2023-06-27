
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from base.models import Blog,Flaticon,Item,Chef,Order, OrderItem

def home(request):
    menu_items = Item.objects.all()
    blogs = Blog.objects.all()
    flaticon = Flaticon.objects.all()
    context = {"items":menu_items,"blogs":blogs,"flaticons":flaticon, }
    return render(request, "index.html", context)

def menu(request):
    flaticon = Flaticon.objects.all()
    menu_items = Item.objects.all()
    context = {"items":menu_items,"flaticons":flaticon}
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

# views for login signup and orders

def add_to_order(request, itemId):
    item = Item.objects.get(pk=itemId)
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, item=item)
    if not created:
        order_item.quantity += 1
        order_item.save()
    return redirect('order')

@login_required
def order(request):
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order_items = order.orderitem_set.all()
    total = sum(item.Item.price * item.quantity for item in order_items)
    return render(request, 'orderpage.html', {'order_items': order_items,'total':total})

# signup form
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup1.html', {'form': form})