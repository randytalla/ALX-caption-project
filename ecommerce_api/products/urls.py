from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)  # Creates endpoints for CRUD operations

urlpatterns = [
    path('', include(router.urls)),  # Include all product-related API endpoints
]
