from rest_framework import serializers

from posts.models import Post


class PostCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "created_at",
            "updated_at",
        ]


class PostListSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username", )

    class Meta:
        model = Post
        fields = [
            "pk",
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
            "pk",
            "title",
            "content",
            "username",
            "created_at",
            "updated_at",
        ]
