# django imports
from django.shortcuts import render

# local application imports
from .models import (
    Profile,
)


def index(request):
    """
    This function renders the index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'app_profiles/index.html', context)


def profile(request, username):
    """
    This function renders the profile page.
    :arg username: The username of the profile to render.
    """
    profile = Profile.objects.get(user__username=username)
    context = {
        'profile': profile,
    }
    return render(request, 'app_profiles/profile.html', context)
