
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from base.models import Blog,Flaticon,Item,Chef,Order, OrderItem

def home(request):
    menu_items = Item.objects.all()
    blogs = Blog.objects.all()
    context = {"items":menu_items,"blogs":blogs}
    return render(request, "index.html", context)

def menu(request):
    menu_items = Item.objects.all()
    context = {"items":menu_items}
    return render(request, "menu.html", context)

def services(request):
    menu_items = Item.objects.all()
    context = {"items":menu_items}
    return render(request, "services.html", context)

def blog(request):
    blog_content = Blog.objects.all()
    context = {"blog_contents": blog_content}
    return render(request, "blog.html", context)

def about(request):
    chef = Chef.objects.all()
    context = {"chefs":chef}
    return render(request, "about.html", context)

def contact(request):
    
    # queryset1= Chef()

    # queryset1.save()
    # data={
    #     'queryset1':queryset1,
    # }
    return render(request, "contact.html")

def cart(request):
    return render(request, "orderpage.html")


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
    context= {'item': item, 'order':order,'order_item':order_item}
    return redirect('order')

#login form
@login_required
def order(request):
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order_items = order.orderitem_set.all()
    total = sum(item.Item.price * item.quantity for item in order_items)
    if not created:
        return redirect('order')
    context={'order_items': order_items,'total':total}
    return render(request, 'orderpage.html', context)

# loginForm
def loginForm(request):
     
     page = 'login'
     #when the user is already logged in they cant access login page via the url
     if request.user.is_authenticated:
         return redirect('home')
     

     if request.method == 'POST':
         userName = request.POST.get('username')
         password = request.POST.get('password')

        #try and check if the user exists in the database
         try:
             user = User.objects.get(username=userName)
         except:
             messages.error(request, 'User Does Not Exist')

        #while the user is found to exist, authenticate the user, make sure password and username match   
         user = authenticate(request, username=userName, password=password)

        #while the fields are not empty and user is found then create a session for the user and redirect them to their homepage
         if user is not None:
             login(request, user)
             return redirect('home')
         else:
             messages.error(request, 'UserName Or Password Does Not Exist')

     context = {'page': page}
     return render(request, 'RegisterLoginForm.html', context) 

#cancel session from database and redirect to homepage
def logoutForm(request):
    logout(request)
    return redirect('home')

#signUp/register form
def registerForm(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Sorry An Error Occurred During Registration')

    context = {'form': form}
    return render(request, 'RegisterLoginForm.html',context)