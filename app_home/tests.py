# django imports
from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_index(self):
        response = self.client.get(reverse('app_home:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertIn(b'<title>Holiday Homes</title>', response.content)
