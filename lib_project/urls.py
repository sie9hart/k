"""lib_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from libra import views
import lib_project.urls

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', views.server, name='server'),
    path("Book", views.Book ),
    path("custs", views.cust ),
    path("Borrow", views.Borrows ),
    path("sform", views.sform ),
    path("sform2", views.sform2 ),
    path("sform3", views.sform3 )



]
