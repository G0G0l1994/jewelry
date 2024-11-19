from django.urls import path

from .views import *

urlpatterns = [path('add_customer/', customer_add,name = 'customer_add'),
               path('', customer_list,name='customer_list'),
               path('<int:pk>/', customer_detail,name='customer_detail'),
               path('<int:pk>/update/', customer_update,name='customer_update'),
               path('<int:pk>/delete/', customer_delete, name='customer_delete')]