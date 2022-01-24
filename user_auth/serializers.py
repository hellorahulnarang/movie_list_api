from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        
    # def create(self, validated_data):
    #     username = validated_data['username']
    #     password = validated_data['password']

    #     user = User.objects.get_or_create(username = username)

    #     # set_password
    #     user[0].set_password(password)
    #     user[0].save()
    #     return user[0]
