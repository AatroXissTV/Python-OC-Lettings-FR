from django.urls import path
from app_profiles.views import (
    index,
    profile,
)


app_name = 'app_profiles'
urlpatterns = [
    path('', index, name='index'),
    path('<str:username>/', profile, name='profile'),
]
