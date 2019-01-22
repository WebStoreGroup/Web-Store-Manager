from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
)
from .models import (
    Item,
    PromoImage,
    StockItem,
    Customer,
    ReviewComment,
    TransactionStatus,
    Transaction,
    TransactionItem
)
from .serializers import (
    ItemSerializer,
    PromoImageSerializer,
    StockItemSerializer,
    CustomerSerializer,
    ReviewCommentSerializer,
    TransactionStatusSerializer,
    TransactionSerializer,
)

# Create your views here.

class PromoImageListView(generics.ListCreateAPIView):
    queryset = PromoImage.objects.all()
    serializer_class = PromoImageSerializer
    permission_classes = (AllowAny, )

class ItemListView(generics.ListCreateAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    search_fields = ('item__name', 'item__description')
    ordering_fields = ('item__rating', 'item__price')

    # TODO : filter amount != 0 for customers
    # def get_queryset(self):
    #     if user is not admin:
    #         return StockItem.objects.filter(amount > 0)
    #     return this.get_queryset()

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ReviewCommentListView(generics.ListCreateAPIView):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer

class TransactionStatusListView(generics.ListCreateAPIView):
    queryset = TransactionStatus.objects.all()
    serializer_class = TransactionStatusSerializer

class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    search_fields = ('customer__name', 'customer__email', 'transaction_items__item__name', 'transaction_items__item__description')
    filter_fields = ('status', )
    ordering_fields = ('status__status', 'datetime')

class TransactionDetailRetrieveView(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
