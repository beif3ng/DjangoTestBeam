from django.urls import path

from .views import (
    UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView,
    ProfileListCreateAPIView, ProfileRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
    OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Users
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update'),

    # Profiles
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-retrieve-update'),

    # Products
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update'),

    # Orders
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-retrieve-update'),
]