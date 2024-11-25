from django.urls import path

from .views import *


urlpatterns = [
    path('', product_list, name='product_list'),
    path('add-product/',add_product,name='add_product'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('<int:pk>/update/', product_update, name='product_update'),
    path('<int:pk>/delete/', product_delete,name='product_delete'),
    path('<int:pk>/update_time/', update_time,name='update_time')
    
    ]