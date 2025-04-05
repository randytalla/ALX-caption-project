from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer


class ProductPagination(PageNumberPagination):
    page_size = 5

class ProductViewSet(viewsets.ModelViewSet):
    """API for CRUD operations on products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Add filtering, searching, and pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Search by product name or category (partial matches allowed)
    search_fields = ['name', 'category']

    # Filtering options
    filterset_fields = ['category', 'price', 'stock_quantity']

    # Ordering options (ascending/descending price)
    ordering_fields = ['price', 'created_at']