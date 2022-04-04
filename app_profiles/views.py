# app_profiles/views.py
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
    Profile,
)

# other imports & constants


def profiles_index(request):
    """
    This function renders the index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'app_profiles/profiles_index.html', context)


def profile(request, username):
    """
    This function renders the profile page.
    """
    profile = Profile.objects.get(username=username)
    context = {
        'profile': profile,
    }
    return render(request, 'app_profiles/profile.html', context)
