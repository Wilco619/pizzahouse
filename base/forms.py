from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_view

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','mobile','zipcode','county']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            'county':forms.Select(attrs={'class':'form-control'}),
        }

class MyPasswordChangeForm(PasswordChangeForm):
    old_password= forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1= forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    
class MyPasswordResetForm(PasswordResetForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))






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