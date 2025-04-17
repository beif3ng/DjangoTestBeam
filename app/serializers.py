from rest_framework import serializers
from .models import User, Profile, Order, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())


    class Meta:
        model = Profile
        fields = ['id', 'user', 'address']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Для записи: ID пользователя
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())  # Для записи: список ID товаров

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'created_at']