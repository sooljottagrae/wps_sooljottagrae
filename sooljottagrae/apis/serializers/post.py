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

    email = serializers.CharField(source="user.email", )
    nickname = serializers.CharField(source="user.nickname", )

    class Meta:
        model = Post
        fields = [
            "pk",
            "title",
            "content",
            "email",
            "nickname",
            "user",
            "created_at",
            "updated_at",
        ]


class PostDetailSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source="user.email", )
    nickname = serializers.CharField(source="user.nickname", )

    class Meta:
        model = Post
        fields = [
            "pk",
            "title",
            "content",
            "email",
            "nickname",
            "created_at",
            "updated_at",
        ]
