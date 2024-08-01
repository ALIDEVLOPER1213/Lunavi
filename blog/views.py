from rest_framework import serializers, generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import ClothesCreateSerializer
from .models import Clothes
from .serializers import ClothesSerializer
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated


class ClothesListAPIView(generics.ListAPIView):
    queryset = Clothes.objects.filter(is_active=True)
    serializer_class = ClothesSerializer


class ClothesCreateAPIView(generics.CreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesCreateSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user
        # data = request.data
        serializer = ClothesSerializer(self.get_queryset())
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategorySerializer(generics.ListAPIView):
    queryset = Clothes.objects.all()
    serializer_class = CategorySerializer
