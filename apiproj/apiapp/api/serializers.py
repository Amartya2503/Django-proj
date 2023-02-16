from typing import Self
from rest_framework import serializers
from apiapp.models import newuser,infodata,tasks
from django.contrib.auth.hashers import make_password

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = newuser
#         fields=[
#             "username",
#             "email",
#             "password",
#             "category",

#         ]
#         extra_kwargs = {"password": {"write_only": True}}
#         password = Self.validated_data["password"]
#         # newuser.set_password(password)
#         # newuser.save()
#         # return newuser

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only = True)
    # password = serializers.CharField(write_only = True,)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = newuser
        fields = ["email", "username", "category", "is_active","password"]

        def create(self,validated_data):
            print(validated_data.username)
            return (validated_data)


class userRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True,)
    class Meta:
        model = newuser
        fields = ["email","username","category","password"]
        
class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = infodata
        fields = '__all__'


class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = '__all__'
