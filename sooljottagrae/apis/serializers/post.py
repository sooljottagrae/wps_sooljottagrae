from rest_framework.serializers import (
        ModelSerializer,
        HyperlinkedIdentityField,
        SerializerMethodField,
        CharField,
)

from .comment import CommentSerializer

from posts.models import Post, Comment


class PostCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            "title",
            "image",
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
    user = SerializerMethodField()

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

    def get_user(self, obj):
        return str(obj.user.email)


class PostDetailSerializer(ModelSerializer):

    email = CharField(source="user.email", )
    nickname = CharField(source="user.nickname", )
    url = post_detail_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "url",
            "pk",
            "title",
            "content",
            "image",
            "user",
            "email",
            "nickname",
            "created_at",
            "updated_at",
            "comments",
        ]

    def get_user(self, obj):
        return str(obj.user.email)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        comment_queryset = obj.comment_set.all()
        comments = CommentSerializer(comment_queryset, many=True).data
        return comments
