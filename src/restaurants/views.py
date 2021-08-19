from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantModelViewSet(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


# class RestaurantLCAPIView(ListCreateAPIView):
#     serializer_class = RestaurantSerializer
#     queryset = Restaurant.objects.all()
#
#
# class RestaurantRUDAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = RestaurantSerializer
#     queryset = Restaurant.objects.all()
