from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Item,
    StockItem,
    Customer,
    TransactionStatus,
    Transaction,
    TransactionItem
)

from .serializers import (
    ItemSerializer,
    StockItemSerializer,
    CustomerSerializer,
    TransactionStatusSerializer,
    TransactionSerializer,
    TransactionItemSerializer,
)

# Create your views here.

class ItemListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    search_fields = ('name', 'description')
    filter_fields = ('name', 'description')

class StockItemListView(generics.ListCreateAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class TransactionStatusListView(generics.ListCreateAPIView):
    queryset = TransactionStatus.objects.all()
    serializer_class = TransactionStatusSerializer

class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer