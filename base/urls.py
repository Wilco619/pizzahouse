from django.urls import path 
from . import views
from .forms import MyPasswordChangeForm, MyPasswordResetForm
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("updateAddress/<int:pk>",views.updateAddress.as_view(),name="updateAddress"),
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

    #user authentication
    path("loginForm/",views.loginForm,name="loginForm"),
    path("registerForm/",views.registerForm,name="registerForm"),
    path("logoutForm/",views.logoutForm,name="logoutForm"),
    path("passwordchange/",auth_view.PasswordChangeView.as_view(template_name='passwordwork.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path("passwordchangedone/",auth_view.PasswordChangeDoneView.as_view(template_name='pwdchangedone.html'), name='passwordchangedone'),
    path("passwordreset/",auth_view.PasswordResetView.as_view(template_name='passwordwork.html',form_class=MyPasswordResetForm), name='/passwordresetdone'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
