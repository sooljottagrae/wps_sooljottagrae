from rest_framework.serializers import (
        ModelSerializer,
        HyperlinkedIdentityField,
        SerializerMethodField,
        CharField,
)

from posts.models import Post


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
        ]

    def get_user(self, obj):
        return str(obj.user.email)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image
    
    def get_html(self, obj):
        return obj.get_markdown()
