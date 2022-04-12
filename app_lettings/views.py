from django.shortcuts import render

from .models import (
    Letting,
)


def index(request):
    """
    This function return the lettings objects in the DB.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'app_lettings/index.html', context)


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
