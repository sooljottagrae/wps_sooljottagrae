from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
        CharField,
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        ValidationError,
)

User = get_user_model()


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "phonenumber",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        phonenumber = validated_data['phonenumber']
        user_obj = User(
                username=username,
                phonenumber=phonenumber,
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()

    class Meta:
        model = User
        fields = [
                'username',
                'password',
                'token',
        ]
        extra_kwargs = {"password": {"write_only": True}}


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
                "id",
                "username",
                "password",
                "phonenumber",
        ]
