from django.urls import path
from .views import order_list, create_order, update_order, delete_order  # create_order funksiyasini import qilish

urlpatterns = [
    path('', order_list, name='order_list'),
    path('create/', create_order, name='create_order'),
     path('update/<int:pk>/', update_order, name='update_order'),
    path('delete/<int:pk>/', delete_order, name='delete_order'),
]
