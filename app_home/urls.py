# app_home/urls.py
# created 04/04/2022 at 15:35 by Antoine 'AatroXiss' BEAUDESSON
# last modified 04/04/2022 at 15:35 by Antoine 'AatroXiss' BEAUDESSON

""" app_lettings/urls.py:
    - *
"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "Copyright 2021, Antoine 'AatroXiss' BEAUDESSON"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "0.0.4"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "antoine.beaudesson@gmail.com"
__status__ = "Development"

# standard library imports

# third party imports

# django imports
from django.urls import path

# local application imports
from app_home.views import home_index

# other imports & constants


app_name = 'app_home'
urlpatterns = [
    path('', home_index, name='index'),
]
