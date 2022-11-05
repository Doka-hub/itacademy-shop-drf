from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

import requests

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['GET'], url_path='products')
    def get_products(self, request, *args, **kwargs):
        instance = self.get_object()
        products = instance.products.all()
        serializer = ProductSerializer(products, many=True)

        url = 'https://httpbin.org/get'
        response = requests.get(url)

        return Response(response.json())
