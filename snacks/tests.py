from django.http import response
from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class TestWorks(TestCase):
    def test_home_response(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response, 200)