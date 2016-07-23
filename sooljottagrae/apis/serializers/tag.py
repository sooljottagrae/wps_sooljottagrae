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

from apis.serializers.post import *


class TagPostSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = [
                'id',
        ]


class AlcoholTagSerializer(ModelSerializer):

    class Meta:
        model = AlcoholTag
        fields = [
                'id',
                'alcohol_name',
        ]


class AlcoholTagDetailSerializer(ModelSerializer):

    class Meta:
        model = AlcoholTag
        fields = [
                'id',
                'alcohol_name',
                'post',
        ]

    def get_post(self, obj):
        post_queryset = obj.post_set.all()
        posts = TagPostSerializer(post_queryset, many=True).data
        return posts


class FoodTagSerializer(ModelSerializer):

    class Meta:
        model = FoodTag
        fields = [
                'id',
                'food_name',
        ]


class FoodTagDetailSerializer(ModelSerializer):

    class Meta:
        model = FoodTag
        fields = [
                'id',
                'food_name',
                'post',
        ]

    def get_post(self, obj):
        post_queryset = obj.post_set.all()
        posts = TagPostSerializer(post_queryset, many=True).data
        return posts


class PlaceTagSerializer(ModelSerializer):

    class Meta:
        model = PlaceTag
        fields = [
                'id',
                'place_name',
        ]


class PlaceTagDetailSerializer(ModelSerializer):

    post = SerializerMethodField()

    class Meta:
        model = PlaceTag
        fields = [
                'id',
                'place_name',
                'post',
        ]

    def get_post(self, obj):
        post_queryset = obj.post_set.all()
        posts = TagPostSerializer(post_queryset, many=True).data
        return posts
