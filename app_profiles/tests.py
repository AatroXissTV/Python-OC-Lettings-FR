# app_profiles/tests.py
# created 01/04/2022 at 10:42 by Antoine 'AatroXiss' BEAUDESSON
# last modified 01/04/2022 at 10:42 by Antoine 'AatroXiss' BEAUDESSON

""" app_profiles/tests.py:
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
from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from django.urls import reverse

# local application imports
from app_profiles.models import Profile

# other imports & constants


class User(AbstractUser):
    pass


class ProfilesTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
            email='testuser@test.com'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='New York',
        )

    def test_profiles_index(self):
        response = self.client.get(reverse('app_profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual("testuser", response.context['profile'].username)

    def test_profiles_detail(self):
        response = self.client.get(reverse('app_profiles:detail', args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual("testuser", response.context['profile'].username)

    def test_profiles_str(self):
        self.assertEqual(str(self.profile), 'testuser')
