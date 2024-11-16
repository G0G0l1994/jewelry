from django.urls import path

from .views import add_product, product_list,product_detail


urlpatterns = [
    path('', product_list, name='product_list'),
    path('add-product/',add_product,name='add_product'),
    path('<int:pk>/', product_detail, name='product_detail')
    ]