from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user_auth.views import UserRegistration

class TestUrls(SimpleTestCase):
    
    def test_registration_url(self):
        url = reverse('user-register')
        self.assertEquals(resolve(url).func.view_class, UserRegistration)