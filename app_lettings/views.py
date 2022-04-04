# app_lettings/views.py
# created 01/04/2022 at 10:42 by Antoine 'AatroXiss' BEAUDESSON
# last modified 01/04/2022 at 10:42 by Antoine 'AatroXiss' BEAUDESSON

""" app_lettings/views.py:
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
from django.shortcuts import render

# local application imports
from .models import (
    Letting,
)

# other imports & constants


def index(request):
    """
    This function returns the index page of the app_lettings.
    """
    return render(request, 'app_lettings/index.html')


def lettings_index(request):
    """
    This function return the lettings objects in the DB.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'app_lettings/lettings_index.html', context)


def letting(request, letting_id):
    """
    This function returns the letting object with the given id.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'app_lettings/letting.html', context)
