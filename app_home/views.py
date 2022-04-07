# app_home/views.py
# created 04/04/2022 at 15:35 by Antoine 'AatroXiss' BEAUDESSON
# last modified 07/04/2022 at 10:50 by Antoine 'AatroXiss' BEAUDESSON

""" app_home/views.py:
    - *
"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "Copyright 2021, Antoine 'AatroXiss' BEAUDESSON"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "0.0.5"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "antoine.beaudesson@gmail.com"
__status__ = "Development"

# standard library imports

# third party imports

# django imports
from django.shortcuts import render

# local application imports

# other imports & constants


def home_index(request):
    return render(request, 'index.html')
