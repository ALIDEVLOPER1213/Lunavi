from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ClothesListAPIView.as_view(), name='clothes-list'),
    path('create.', ClothesCreateAPIView.as_view(), name='clothes-create'),
  ]
