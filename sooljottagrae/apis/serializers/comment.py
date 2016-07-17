from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        CharField,
)

from posts.models import Comment


class CommentModelSerializer(ModelSerializer):

    nickname = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "absolute_url",

            "user",
            "nickname",
            "content",
        ]

    def get_user(self, obj):
        return str(obj.user.nickname)
