from rest_framework.serializers import (
        ModelSerializer,
        HyperlinkedIdentityField,
        HyperlinkedModelSerializer,
        SerializerMethodField,
        CharField,
)

from posts.models import Post
from tags.models import (
        AlcoholTag,
        FoodTag,
        PlaceTag,
)

alcohol_tag_detail_url = HyperlinkedIdentityField(
        view_name='apis:tags:alcohol-detail',
        lookup_field='pk',
)

food_tag_detail_url = HyperlinkedIdentityField(
        view_name='apis:tags:food-detail',
        lookup_field='pk',
)

place_tag_detail_url = HyperlinkedIdentityField(
        view_name='apis:tags:place-detail',
        lookup_field='pk',
)


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
                'id',
                'content',
        ]


class AlcoholTagSerializer(ModelSerializer):

    class Meta:
        model = AlcoholTag
        fields = [
                'id',
                'alcohol_name',
        ]


class AlcoholTagDetailSerializer(ModelSerializer):
    posts = SerializerMethodField()

    class Meta:
        model = AlcoholTag
        fields = [
                'id',
                'alcohol_name',
                'posts',
        ]

    def get_posts(self, obj):
        post_queryset = obj.post_set.all()
        posts = PostSerializer(post_queryset, many=True).data
        return posts


class FoodTagSerializer(ModelSerializer):
    url = food_tag_detail_url

    class Meta:
        model = FoodTag
        fields = [
                'url',
                'id',
                'food_name',
        ]


class FoodTagDetailSerializer(ModelSerializer):
    posts = SerializerMethodField()

    class Meta:
        model = FoodTag
        fields = [
                'id',
                'food_name',
                'posts',
        ]

    def get_posts(self, obj):
        post_queryset = obj.post_set.all()
        posts = PostSerializer(post_queryset, many=True).data
        return posts


class PlaceTagSerializer(ModelSerializer):
    url = place_tag_detail_url

    class Meta:
        model = PlaceTag
        fields = [
                'url',
                'id',
                'place_name',
        ]


class PlaceTagDetailSerializer(ModelSerializer):

    posts = SerializerMethodField()

    class Meta:
        model = PlaceTag
        fields = [
                'id',
                'place_name',
                'posts',
        ]

    def get_posts(self, obj):
        post_queryset = obj.post_set.all()
        posts = PostSerializer(post_queryset, many=True).data
        return posts
