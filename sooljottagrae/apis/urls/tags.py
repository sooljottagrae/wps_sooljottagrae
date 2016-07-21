from django.conf.urls import url, include

from apis.views.tag import *

urlpatterns = [
        url(r'^alcohol/$', AlcoholTagListAPIView.as_view(), name="alcohol-list"),
        url(r'^food/$', FoodTagListAPIView.as_view(), name="food-list"),
        url(r'^place/$', PlaceTagListAPIView.as_view(), name="place-list"),
        ]
