from rest_framework import serializers
from .models import Clothes


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


class ClothesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'

class ClothesUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150, required=False)
    description = serializers.CharField(max_length=10000, required=False)
    image = serializers.ImageField(use_url=True, allow_empty_file=True, required=False)
    price = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance