from django.contrib import admin
from django.urls import path,include
from config.views import  main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main),

    path('', include('board.urls')),
]
