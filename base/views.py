
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from . forms import CustomerProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from base.models import Blog,Flaticon,Product,Chef,Customer

def home(request):
    menu_products = Product.objects.all()
    blogs = Blog.objects.all()
    context = {"products":menu_products,"blogs":blogs}
    return render(request, "index.html", context)

def menu(request):
    menu_products = Product.objects.all()
    context = {"products":menu_products}
    return render(request, "menu.html", context)

def services(request):
    menu_products = Product.objects.all()
    context = {"products":menu_products}
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


#for both post and get methods in a function use a class
class ProfileView(View):
    def get(self,request):
         add = 'create'
         form = CustomerProfileForm()
         return render(request, "profilepage.html",locals())
    def post(self,request):
         add = 'create'
         form = CustomerProfileForm(request.POST)
         if form.is_valid():
             user = request.user
             name = form.cleaned_data['name']
             locality = form.cleaned_data['locality']
             city = form.cleaned_data['city']
             mobile = form.cleaned_data['mobile']
             zipcode = form.cleaned_data['zipcode']
             county = form.cleaned_data['county']

             reg= Customer(user=user, name=name,locality=locality, city=city, mobile=mobile, zipcode=zipcode, county=county)
             reg.save()
             messages.success(request,"Congratulations! Profile Saved Successfully")
         else:
             messages.warning(request,"Invalid Data Input")
             context={'add':add}
         return render(request, "profilepage.html",locals(context))

def address(request):
    add = 'address'
    addss = Customer.objects.filter(user=request.user)
    context = {'add':add,'addss':addss}
    return render(request, "profilepage.html",context)

class updateAddress(View):
    def  get(self,request,pk):
        adds = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=adds)
        add = 'upup'
        return render(request, 'profilepage.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
             adds = Customer.objects.get(pk=pk)
             adds.name = form.cleaned_data['name']
             adds.locality = form.cleaned_data['locality']
             adds.city = form.cleaned_data['city']
             adds.mobile = form.cleaned_data['mobile']
             adds.zipcode = form.cleaned_data['zipcode']
             adds.county = form.cleaned_data['county']

             adds.save()
             messages.success(request,"Congratulations! Profile Updated Successfully")
        else:
             messages.warning(request,"Invalid Data Input")
        return redirect('address')



##########
# loginForm
def loginForm(request):
     
     page = 'login'
     #when the user is already logged in they cant access login page via the url
     if request.user.is_authenticated:
         return redirect('home')
     

     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

        #try and check if the user exists in the database
         try:
             user = User.objects.get(username=username)
         except:
             messages.error(request, 'User Does Not Exist')

        #while the user is found to exist, authenticate the user, make sure password and username match   
         user = authenticate(request, username=username, password=password)

        #while the fields are not empty and user is found then create a session for the user and redirect them to their homepage
         if user is not None:
             login(request, user)
             return redirect('profile')
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