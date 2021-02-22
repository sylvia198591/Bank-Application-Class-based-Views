"""Bank URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import *
from Kiosk import views
from Kiosk.views import *

urlpatterns = [
    path('Addaccount', views.createAccount.as_view(), name="Account_create"),
    path('AddTrans', views.createTrans.as_view(), name="Trans_create"),
    path('Datewise', views.createDatewise.as_view(), name="Datewise_create"),
    path('Viewaccount', views.viewAccount.as_view(), name="Account_view"),
    path('Updateaccount/<int:pk>', views.updateAccount.as_view(), name="Account_update"),
    path('Deleteaccount/<int:pk>', views.deleteAccount.as_view(), name="Account_delete"),
    path('AddTransfer', views.createTransfer.as_view(), name="Account_transfer"),
    path('Spend', spendanalysis, name="Spend_Analyser"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

