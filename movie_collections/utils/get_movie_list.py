import requests
from django.conf import settings
from rest_framework.response import Response
from requests.auth import HTTPBasicAuth
from django.http import JsonResponse


def get_movie_list(page_number):
    try:
        third_party_api_url = 'https://demo.credy.in/api/v1/maya/movies/'
        if page_number is not None:
            third_party_api_url += f'?page={page_number}'

        # Basic Authentication
        basic = HTTPBasicAuth(settings.MOVIE_API_USERNAME,settings.MOVIE_API_PASSWORD)
        response = requests.get(third_party_api_url, auth=basic)

        if response.status_code==200:  
            response_data = response.json()        
            return Response(response_data)
    except :
        return Response(
            {
                'error': 'Please check your Internet'
            }
        )