from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lettings/', include('app_lettings.urls')),
    path('profiles/', include('app_profiles.urls')),
]
