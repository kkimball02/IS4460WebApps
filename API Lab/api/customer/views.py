from django.shortcuts import render
from rest_framework import generics
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

##CustomerListCreateView
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

##CustomerDetailView
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

##OrderListCreateView
class OrderListCreateView(generics.ListCreateAPIView):
     
     queryset = Order.objects.all()
     serializer_class = OrderSerializer

##OrderDetailView
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
     
     queryset = Order.objects.all()
     serializer_class = OrderSerializer

