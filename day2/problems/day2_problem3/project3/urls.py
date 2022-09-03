

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('throw_catch/', include('throw_catch.urls')),
    
]
