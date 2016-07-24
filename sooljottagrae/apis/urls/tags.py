from django.conf.urls import url, include

from apis.views.tag import *

urlpatterns = [
        url(r'^alcohol/$', AlcoholTagListAPIView.as_view(), name="alcohol-list"),
        url(r'^alcohol/create/$', AlcoholTagCreateAPIView.as_view(), name="alcohol-create"),
        url(r'^alcohol/(?P<pk>\d+)/$', AlcoholTagDetailAPIView.as_view(), name="alcohol-detail"),
        url(r'^alcohol/(?P<pk>\d+)/update/$', AlcoholTagUpdateAPIView.as_view(), name="alcohol-update"),
        url(r'^alcohol/(?P<pk>\d+)/delete/$', AlcoholTagDeleteAPIView.as_view(), name="alcohol-delete"),

        url(r'^food/$', FoodTagListAPIView.as_view(), name="food-list"),
        url(r'^food/create/$', FoodTagCreateAPIView.as_view(), name="food-create"),
        url(r'^food/(?P<pk>\d+)/$', FoodTagDetailAPIView.as_view(), name="food-detail"),
        url(r'^food/(?P<pk>\d+)/update/$', FoodTagUpdateAPIView.as_view(), name="food-update"),
        url(r'^food/(?P<pk>\d+)/delete/$', FoodTagDeleteAPIView.as_view(), name="food-delete"),

        url(r'^place/$', PlaceTagListAPIView.as_view(), name="place-list"),
        url(r'^place/create/$', PlaceTagCreateAPIView.as_view(), name="place-create"),
        url(r'^place/(?P<pk>\d+)/$', PlaceTagDetailAPIView.as_view(), name="place-detail"),
        url(r'^place/(?P<pk>\d+)/update/$', PlaceTagUpdateAPIView.as_view(), name="place-update"),
        url(r'^place/(?P<pk>\d+)/delete/$', PlaceTagDeleteAPIView.as_view(), name="place-delete"),
        ]
