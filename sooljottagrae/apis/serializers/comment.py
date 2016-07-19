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
