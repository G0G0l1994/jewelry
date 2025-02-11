from rest_framework.viewsets import ReadOnlyModelViewSet

from product.models import Product
from .serializers import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

