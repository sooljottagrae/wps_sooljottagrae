from rest_framework.serializers import (
        ModelSerializer,
        HyperlinkedIdentityField,
        SerializerMethodField,
        CharField,
)

from .comment import CommentSerializer
from .tag import AlcoholTagSerializer
from .user import UserModelSerializer

from posts.models import Post, Comment
from tags.models import AlcoholTag, FoodTag, PlaceTag


class PostCreateUpdateSerializer(ModelSerializer):
    alcohol_tag = CharField(source="alcoholtag_set")

    class Meta:
        model = Post
        fields = [
            "image",
            "content",
            "alcohol_tag",
            "created_at",
            "updated_at",
        ]

post_detail_url = HyperlinkedIdentityField(
        view_name='apis:posts:detail',
        lookup_field='pk',
)


class PostListSerializer(ModelSerializer):

    url = post_detail_url
    user = UserModelSerializer(read_only=True)
    comments_number = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "url",
            "pk",
            "content",
            "image",
            "user",
            "created_at",
            "updated_at",
            "comments_number",
        ]

    def get_user(self, obj):
        return str(obj.user.email)

    def get_comments_number(self, obj):
        if obj.comment_set.all():
            return obj.comment_set.count()
        return 0


class PostDetailSerializer(ModelSerializer):

    url = post_detail_url
    user = UserModelSerializer(read_only=True)
    image = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "url",
            "pk",
            "content",
            "image",
            "user",
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

    def get_alcohol_tag(self, obj):
        alcoholtag_queryset = obj.alcoholtag_set.all()
        alcoholtag = AlcoholTagSerializer(alcoholtag_queryset).data
        return alcoholtag

    def get_food_tag(self, obj):
        foodtag_queryset = obj.foodtag_set.all()
        foodtag = FoodTagSerializer(foodtag_queryset).data
        return foodtag

    def get_place_tag(self, obj):
        placetag_queryset = obj.placetag_set.all()
        placetag = PlaceTagSerializer(placetag_queryset).data
        return placetag
