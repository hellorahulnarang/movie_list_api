from django.test import TestCase, Client
from django.urls import reverse
from user_auth.models import User
import json
from rest_framework import status

class TestViews(TestCase):
    #initial configuration   
    def setUp(self):
        self.client = Client()

    def test_user_registration_GET(self):
        client = self.client
        response = client.get(reverse("user_register"))
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_user_registration_POST(self):
        client = self.client
        response = client.post(reverse("user_register"),{
            "username":"testuser",
            "password": "fooboo12"
        })
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(User.objects.first().username, "testuser")

    #repeating same username
    def test_user_repeation(self):
        client = self.client
        response = client.post(reverse("user_register"),{
            "username":"rahulkumarnarang",
            "password": "test@123"
        })
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(User.objects.first().username, "repeatuser")

        response = client.post(reverse("user_register"),{
            "username":"rahulkumarnarang",
            "password": "test@123"
        })
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)


   #register without password
    def test_user_registration_empty_password_POST(self):
        client = self.client
        response = client.post(reverse("user_register"),{
            "username":"newuser",
            "password": ""
        })
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    #register without username
    def test_user_registration_empty_username_POST(self):
        client = self.client
        response = client.post(reverse("user_register"),{
            "username":"",
            "password": "test@123"
        })
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

