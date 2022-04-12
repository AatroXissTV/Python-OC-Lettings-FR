from django.urls import path
from app_home.views import home_index


app_name = 'app_home'
urlpatterns = [
    path('', home_index, name='index'),
]
