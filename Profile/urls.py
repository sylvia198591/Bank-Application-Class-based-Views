
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
from Profile.views import *
# from Userdetail.views import *
from Userdetail.views import *
from django.contrib.auth import views as auth_views
from django.urls import path
# app_name='profile'
urlpatterns = [
    # path("create_profile", views.createProfile.as_view(), name="crprofile"),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)