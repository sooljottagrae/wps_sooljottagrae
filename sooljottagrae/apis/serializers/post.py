from rest_framework import serializers

from posts.models import Post


class PostCreateUpdateSerializer(serializers.ModelSerializer):

    # username = serializers.CharField(source="user.username", )

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "user",
            "created_at",
            "updated_at",
        ]


class PostListSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username", )

    class Meta:
        model = Post
        fields = [
            "post_id",
            "title",
            "content",
            "username",
            "user",
            "created_at",
            "updated_at",
        ]


class PostDetailSerializer(serializers.ModelSerializer):

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
