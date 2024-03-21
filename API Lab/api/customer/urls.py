from django.urls import path
from customer.views import CustomerListCreateView, CustomerDetailView, OrderDetailView, OrderListCreateView

urlpatterns = [
    path('customer/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('order/', OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail')
]
