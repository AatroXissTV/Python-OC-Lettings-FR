# django imports
from django.test import TestCase
from django.urls import reverse

# app imports
from .models import (
    Address,
    Letting
)


class LettingsPageTests(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number='1',
            street='Test Street',
            city='Test City',
            state='Test State',
            zip_code='12345',
            country_iso_code='US',
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address,
        )

    def test_lettings_index(self):
        response = self.client.get(reverse('app_lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_lettings/index.html')
        self.assertIn(b'<title>Lettings</title>', response.content)

    def test_lettings_detail(self):
        response = self.client.get(reverse('app_lettings:letting', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_lettings/letting.html')

    def test_lettings_models(self):
        assert str(self.address) == f'{self.address.number} {self.address.street}'
        assert str(self.letting) == f'{self.letting.title}'
