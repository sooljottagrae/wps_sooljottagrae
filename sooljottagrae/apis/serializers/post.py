from rest_framework.serializers import (
        ModelSerializer,
        HyperlinkedIdentityField,
        SerializerMethodField,
        CharField,
)

from .comment import CommentSerializer
from .tag import (
        AlcoholTagSerializer,
        AlcoholTagGeneralSerializer,
        FoodTagSerializer,
        FoodTagGeneralSerializer,
        PlaceTagSerializer,
        PlaceTagGeneralSerializer,

)
from .user import UserModelSerializer

from posts.models import Post, Comment
from tags.models import AlcoholTag, FoodTag, PlaceTag

post_detail_url = HyperlinkedIdentityField(
        view_name='apis:posts:detail',
        lookup_field='pk',
)


class PostCreateSerializer(ModelSerializer):
    alcohol_tag = CharField(source="alcoholtag_set")
    food_tag = CharField(source="foodtag_set")
    place_tag = CharField(source="placetag_set")

    class Meta:
        model = Post
        fields = [
            "image",
            "content",
            "alcohol_tag",
            "food_tag",
            "place_tag",
            "created_at",
            "updated_at",
        ]


class PostUpdateSerializer(ModelSerializer):
    alcohol_tag = AlcoholTagGeneralSerializer(source="alcoholtag_set", many=True)
    food_tag = FoodTagGeneralSerializer(source="foodtag_set", many=True)
    place_tag = PlaceTagGeneralSerializer(source="placetag_set", many=True)

    class Meta:
        model = Post
        fields = [
            "image",
            "content",
            "alcohol_tag",
            "food_tag",
            "place_tag",
            "created_at",
            "updated_at",
        ]


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    comments_number = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "url",
            "pk",
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

    alcohol_tag = SerializerMethodField()
    food_tag = SerializerMethodField()
    place_tag = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "url",
            "pk",
            "content",
            "image",
            "alcohol_tag",
            "food_tag",
            "place_tag",
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
        alcoholtags = AlcoholTagSerializer(alcoholtag_queryset, many=True).data
        return alcoholtags

    def get_food_tag(self, obj):
        foodtag_queryset = obj.foodtag_set.all()
        foodtags = FoodTagSerializer(foodtag_queryset, many=True).data
        return foodtags

    def get_place_tag(self, obj):
        placetag_queryset = obj.placetag_set.all()
        placetags = PlaceTagSerializer(placetag_queryset, many=True).data
        return placetags
