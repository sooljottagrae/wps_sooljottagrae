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
    url = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
                'url',
                'id',
                'content',
        ]

    def get_url(self, obj):
        absolute_url = Post.get_absolute_api_url(obj)
        full_url = "https://" + "sooljotta.com" + absolute_url
        return full_url


class AlcoholTagSerializer(ModelSerializer):
    url = SerializerMethodField()

    class Meta:
        model = AlcoholTag
        fields = [
                'url',
                'id',
                'alcohol_name',
        ]

    def get_url(self, obj):
        absolute_url = AlcoholTag.get_absolute_api_url(obj)
        full_url = "https://" + "sooljotta.com" + absolute_url
        return full_url


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
    url = SerializerMethodField()

    class Meta:
        model = FoodTag
        fields = [
                'url',
                'id',
                'food_name',
        ]

    def get_url(self, obj):
        absolute_url = FoodTag.get_absolute_api_url(obj)
        full_url = "https://" + "sooljotta.com" + absolute_url
        return full_url


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
    url = SerializerMethodField()

    class Meta:
        model = PlaceTag
        fields = [
                'url',
                'id',
                'place_name',
        ]

    def get_url(self, obj):
        absolute_url = PlaceTag.get_absolute_api_url(obj)
        full_url = "https://" + "sooljotta.com" + absolute_url
        return full_url


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
