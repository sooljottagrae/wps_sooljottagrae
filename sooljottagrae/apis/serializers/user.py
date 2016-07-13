from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
        EmailField,
        CharField,
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        ValidationError,
)

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    password = CharField(label="비밀번호")
    password2 = CharField(label="비밀번호 확인")

    class Meta:
        model = User
        fields = [
            "email",
            "nickname",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get("email")

        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("이미 사용중인 이메일입니다")
        return value

    def validate_password(self, value):
        data = self.get_initial()
        password1 = data.get("password")
        password2 = value
        if password1 != password2:
            raise ValidationError("비밀번호가 일치하지 않습니다")
        return value

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        nickname = validated_data['nickname']
        user_obj = User(
                email=email,
                nickname=nickname,
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
                'email',
                'nickname',
                'password',
                'token',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        password = data["password"]
        if not email:
            raise ValidationError("로그인하려면 사용자 이름을 입력하세요")

        user = User.objects.filter(
                Q(email=email)
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
                "nickname",
                "email",
                "password",
        ]
