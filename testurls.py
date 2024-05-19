"""
test URL Configuration for juntagrico_badges development
"""
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('juntagrico.urls')),
    path('', include('juntagrico_badges.urls')),
    path('impersonate/', include('impersonate.urls')),
]
