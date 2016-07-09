from rest_framework import serializers

from posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username", )

    class Meta:
        model = Post 
        fields = [
            "post_id",
            "title",
            "content",
            "username",
            "created_at",
            "updated_at",
        ]
