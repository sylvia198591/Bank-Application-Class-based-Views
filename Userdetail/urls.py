
"""OnlineMobileShop URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.shortcuts import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Userdetail import views
from Userdetail.views import *
from django.contrib.auth import views as auth_views
from django.urls import path
# app_name='udtl'
urlpatterns = [
    # path("register", views.createUser.as_view(), name="register"),

    path('', userHome, name="userhome"),
    path('upd/<int:pk>', views.userUpdate.as_view(), name='upd'),
    path('login', auth_views.LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='Userdetail/login_out.html'
        ), 
        name='login'
    ),
    path('userlogout', auth_views.LogoutView.as_view(
            next_page='userhome'
            ),
            name='userlogout'
        ),
    path(
            'change-password/',
            auth_views.PasswordChangeView.as_view(
                template_name='Userdetail/change-password.html',
                success_url =reverse_lazy('login')
            ),
            name='change_password'
        ),
# Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='Userdetail/password-reset/password_reset.html',
             subject_template_name='Userdetail/password-reset/password_reset_subject.txt',
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='Userdetail/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='Userdetail/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='Userdetail/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    # path('', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('delprof/<int:pk>', views.deleteProfile.as_view(), name="delprofile"),
    path('create_profile/<int:pk>', views.createProfile.as_view(), name="crprofile"),
    # path("userlogout", userLogout, name="userlogout"),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

