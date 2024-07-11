
from rest_framework import serializers, generics, status
from rest_framework.response import Response
from .serializer import ClothesCreateSerializer
from .models import Clothes
from .serializer import ClothesSerializer, ClothesUpdateSerializer
from rest_framework.permissions import IsAuthenticated



class ClothesListAPIView(generics.ListAPIView):
    queryset = Clothes.objects.filter(is_active=True)
    serializer_class = ClothesSerializer



class ClothesRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Clothes.objects.filter(is_active=True)
    serializer_class = ClothesSerializer




class ClothesCreateAPIView(generics.CreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesCreateSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = ClothesSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClothesUpdateAPIView(generics.UpdateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesUpdateSerializer

    def put(self, request, pk):
        try:
            user = request.user
            data = request.data
            product = Clothes.objects.filter(id=pk, owner=user).first()
            if product:
                serializer = ClothesUpdateSerializer(data=data, partial=True)
                if serializer.is_valid():
                    serializer.update(product, serializer.validated_data)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "You don't have permission"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class ClothesDeleteAPIView(generics.DestroyAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

    def delete(self, request, pk):
        try:
            user = request.user
            product = Clothes.objects.filter(id=pk, owner=user)
            product.delete()
            return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class ClothesOwnerAPIView(generics.ListAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

    def get(self, request):
        user = request.user
        products = Clothes.objects.filter(owner=user)
        serializer = ClothesSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)