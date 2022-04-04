# app_lettings/models.py
# created 01/04/2022 at 10:42 by Antoine 'AatroXiss' BEAUDESSON
# last modified 01/04/2022 at 10:42 by Antoine 'AatroXiss' BEAUDESSON

""" app_lettings/models.py:
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
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models

# local application imports

# other imports & constants


class Address(models.Model):
    """
    This class represents the address in the DB.
    - Attributes:
        number (int): the number of the address.
        street (str): the street of the address.
        city (str): the city of the address.
        state (str): the state of the address.
        zip_code (int): the zip code of the address.
        country_iso_code (str): the country iso code of the address.
    """
    # Fields
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    # Methods
    def __str__(self):
        return f'{self.number} {self.street}'

    # Meta
    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    This class represents the letting in the DB.
    - Attributes:
        title (str): the title of the letting.
        address (FK:Address): the address of the letting.
    """
    # Fields
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    # Methods
    def __str__(self):
        return self.title
