from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductViewSet

product_list = ProductViewSet.as_view({'get': 'list'})
product_detail = ProductViewSet.as_view({'get': 'retrieve'})


urlpatterns = format_suffix_patterns([
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail,name='product-detail')],
    )