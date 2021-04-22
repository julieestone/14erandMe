from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hikes/', include('hike.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
