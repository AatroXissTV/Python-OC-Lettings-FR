# app_profiles/urls.py
# created 01/04/2022 at 10:42 by Antoine 'AatroXiss' BEAUDESSON
# last modified 01/04/2022 at 10:42 by Antoine 'AatroXiss' BEAUDESSON

""" app_profiles/urls.py:
    - *
"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "Copyright 2021, Antoine 'AatroXiss' BEAUDESSON"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "0.0.3"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "antoine.beaudesson@gmail.com"
__status__ = "Development"

# standard library imports

# third party imports

# django imports
from django.urls import path

# local application imports
from app_profiles.views import (
    profiles_index,
    profile,
)

# other imports & constants


app_name = 'app_profiles'
urlpatterns = [
    path('', profiles_index, name='index'),
    path('<str:username>/', profile, name='detail'),
]
