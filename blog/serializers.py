from rest_framework import serializers
from .models import Clothes, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ClothesDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Clothes
        fields = ['id', 'title', 'description', 'price', 'category']


class ClothesSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Clothes
        fields = '__all__'


class ClothesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'


class ClothesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['id', 'name', 'price']
