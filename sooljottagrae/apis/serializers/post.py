from rest_framework.serializers import (
        ModelSerializer,
        HyperlinkedIdentityField,
        CharField,
)

from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "created_at",
            "updated_at",
        ]

post_detail_url = HyperlinkedIdentityField(
        view_name='apis:posts:detail',
        lookup_field='pk',
)


class PostListSerializer(ModelSerializer):

    email = CharField(source="user.email", )
    nickname = CharField(source="user.nickname", )
    url = post_detail_url

    class Meta:
        model = Post
        fields = [
            "url",
            "pk",
            "title",
            "content",
            "email",
            "nickname",
            "user",
            "created_at",
            "updated_at",
        ]


class PostDetailSerializer(ModelSerializer):

    email = CharField(source="user.email", )
    nickname = CharField(source="user.nickname", )
    url = post_detail_url

    class Meta:
        model = Post
        fields = [
            "url",
            "pk",
            "title",
            "content",
            "email",
            "nickname",
            "created_at",
            "updated_at",
        ]
