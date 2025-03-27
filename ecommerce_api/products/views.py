from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    - GET (list, retrieve)
    - POST (create)
    - PUT/PATCH (update)
    - DELETE (delete)
    """
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow anyone to view, but only authenticated users to edit
