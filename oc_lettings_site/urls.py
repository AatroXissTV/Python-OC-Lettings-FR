from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    division_by_zero = 1 / 0  # noqa


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', include('app_home.urls')),
    path('lettings/', include('app_lettings.urls')),
    path('profiles/', include('app_profiles.urls')),
    path('admin/', admin.site.urls),
]
