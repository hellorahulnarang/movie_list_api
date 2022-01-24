from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from .token import get_tokens_for_user


class UserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_serializer = UserSerializer(data = request.data)
            
        if user_serializer.is_valid():
            user = user_serializer.save()
            user.set_password(user_serializer.validated_data['password'])
            user.save()

            # user = user_serializer.create(validated_data= user_serializer.validated_data)
            
            # generating simples_JWT access_token
            access_token = get_tokens_for_user(user)    
            return Response(
                {
                    "access_token": access_token['access']
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                'error': user_serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

        
