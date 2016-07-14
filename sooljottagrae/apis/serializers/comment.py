from rest_framework import serializers

from posts.models import Comment


class CommentModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.nickname", )

    class Meta:
        model = Comment
        fields = [
            "nickname",

            "content",
        ]
