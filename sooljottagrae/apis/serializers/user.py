from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q

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
    username = CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
                'username',
                'password',
                'token',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data["password"]
        if not username:
            raise ValidationError("로그인하려면 사용자 이름을 입력하세요")

        user = User.objects.filter(
                Q(username=username)
                ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("유효하지 않은 사용자 이름 또는 비밀번호 입니다. 다시 시도해 주세요.")
        
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("유효하지 않은 비밀번호입니다. 다시 시도해 주세요")
        
        data["token"] = "SOME RANDOM TOKEN"    
        return data


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
                "id",
                "username",
                "password",
                "phonenumber",
        ]
