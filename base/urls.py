from django.urls import path 
from . import views, forms
from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
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
    path("loginForm/",forms.loginForm,name="loginForm"),
    path("registerForm/",forms.registerForm,name="registerForm"),
    path("logoutForm/",forms.logoutForm,name="logoutForm"),
    #password change 
    path("passwordchange/",auth_view.PasswordChangeView.as_view(template_name='pwdchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path("passwordchangedone/",auth_view.PasswordChangeDoneView.as_view(template_name='pwdchangedone.html'), name='passwordchangedone'),
    #password reset
    path("passwordreset/",auth_view.PasswordResetView.as_view(template_name='pwdreset.html',form_class=MyPasswordResetForm), name='passwordreset'),
    path("passwordreset/done/",auth_view.PasswordResetDoneView.as_view(template_name='pwdresetdone.html'), name='password_reset_done'),
    path("passwordresetconfirm/<uidb64>/<token>/",auth_view.PasswordResetConfirmView.as_view(template_name='pwdresetConfirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path("passwordresetcomplete/",auth_view.PasswordResetCompleteView.as_view(template_name='pwdresetcomplete.html'), name='password_reset_complete'),
    
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
