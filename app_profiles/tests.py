# django imports
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# app imports
from .models import (
    Profile
)


class ProfilePageTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
            email='test_user@test.com'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Test City',
        )

    def test_profile_index(self):
        response = self.client.get(reverse('app_profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_profiles/index.html')
        self.assertIn(b'<title>Profiles</title>', response.content)

    def test_profile_detail(self):
        response = self.client.get(reverse('app_profiles:profile', args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_profiles/profile.html')

    def test_profile_models(self):
        assert str(self.profile) == f'{self.profile.user.username}'
