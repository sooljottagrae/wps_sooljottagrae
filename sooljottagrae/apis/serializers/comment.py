from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        CharField,
)

from posts.models import Comment


class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",

            "user",
            "content",
        ]

    def get_user(self, obj):
        return str(obj.user.nickname)

class CommentCreateSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
