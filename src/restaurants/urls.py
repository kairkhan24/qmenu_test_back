from django.urls import path

from . import views


urlpatterns = [
    path('restaurants/', views.RestaurantModelViewSet.as_view({'get': 'list',
                                                               'post': 'create'})),
    path('restaurants/<int:pk>/', views.RestaurantModelViewSet.as_view({'get': 'retrieve',
                                                                        'patch': 'partial_update',
                                                                        'put': 'update',
                                                                        'delete': 'destroy'})),
    # path('restaurants/', views.RestaurantLCAPIView.as_view()),
    # path('restaurants/<int:pk>/', views.RestaurantRUDAPIView.as_view()),
]

