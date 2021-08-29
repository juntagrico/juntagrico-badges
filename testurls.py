"""
test URL Configuration for juntagrico_badges development
"""
from django.urls import include, path
from django.contrib import admin
from juntagrico import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('juntagrico.urls')),
    path(r'', include('juntagrico_badges.urls')),
    path(r'', views.home),
]
