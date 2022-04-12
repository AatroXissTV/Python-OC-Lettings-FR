from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('app_home.urls')),
    path('lettings/', include('app_lettings.urls')),
    path('profiles/', include('app_profiles.urls')),
    path('admin/', admin.site.urls),
]
