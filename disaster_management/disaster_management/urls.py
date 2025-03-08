from django.contrib import admin
from django.urls import path,include
from . import views  # Import views from the current app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
   
]