"""palproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import url
from clients.views import dashboard, register
from clients.views import clientsListView

urlpatterns = [
    path('admin/', admin.site.urls),
]

# clients/urls.py

from django.conf.urls import include, url
from clients.views import dashboard, register

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
     url(r"^", include("clients.urls")),
      url(r"^admin/", admin.site.urls),
]




urlpatterns = [
    path('clientslists', clientsListView.as_view(), name='clients-list'),
]