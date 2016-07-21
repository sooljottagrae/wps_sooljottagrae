from rest_framework.serializers import (
        ModelSerializer,
        HyperlinkedIdentityField,
        SerializerMethodField,
        CharField,
)

from tags.models import (
        AlcoholTag,
        FoodTag,
        PlaceTag,
)


class AlcoholTagSerializer(ModelSerializer):

    class Meta:
        model = AlcoholTag
        fields = [
                'id',
                'alcohol_name',
        ]


class FoodTagSerializer(ModelSerializer):

    class Meta:
        model = FoodTag
        fields = [
                'id',
                'food_name',
        ]


class PlaceTagSerializer(ModelSerializer):

    class Meta:
        model = PlaceTag
        fields = [
                'id',
                'place_name',
        ]
