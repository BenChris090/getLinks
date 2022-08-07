from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ('pk', 'f_name', 'm_name', 'l_name', 'email', 'username', 'password', 'registrationDate')