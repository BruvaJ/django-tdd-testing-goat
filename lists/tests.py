from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.

# to check this is getting run
class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
