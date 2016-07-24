from django.contrib.sites.models import Site

from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        CharField,
)

from posts.models import Comment

comment_detail_url = HyperlinkedIdentityField(
        view_name='apis:comments:detail',
        lookup_field='id',
)


class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    url = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "url",
            "id",
            "post",
            "user",
            "content",
        ]

    def get_user(self, obj):
        return str(obj.user.nickname)

    def get_url(self, obj):
        absolute_url = Comment.get_absolute_api_url(obj)
        full_url = "https://" + "sooljotta.com" + absolute_url
        return full_url


class CommentCreateSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            "content",
        ]


class CommentEditSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
        ]


class CommentDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    url = comment_detail_url

    class Meta:
        model = Comment
        fields = [
            "url",
            "id",
            "post",
            "user",
            "content",
        ]

    def get_user(self, obj):
        return str(obj.user.nickname)
