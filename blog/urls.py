from django.urls import path
from .views import *

urlpatterns = [
    path('list', ClothesListAPIView.as_view(), name='clothes-list'),
    path('<int:pk>', ClothesRetrieveAPIView.as_view(), name='clothes-retrieve'),
    path('create.', ClothesCreateAPIView.as_view(), name='clothes-create'),
    path('update/<int:pk>', ClothesUpdateAPIView.as_view(), name='clothes-update'),
    path('delete/<int:pk>', ClothesDeleteAPIView.as_view(), name='clothes-delete'),
    path('owners', ClothesOwnerAPIView.as_view(), name='clothes-owners')
]