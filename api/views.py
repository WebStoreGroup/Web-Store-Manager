from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend

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
from .permissions import (
    ReadOnly,
    IsAdmin,
    IsOwner,
)

# Create your views here.

class PromoImageListView(generics.ListCreateAPIView):
    queryset = PromoImage.objects.all()
    serializer_class = PromoImageSerializer
    permission_classes = (IsAdmin|ReadOnly,)

class ItemListView(generics.ListCreateAPIView):
    queryset = StockItem.objects.all()
    serializer_class = StockItemSerializer
    permission_classes = (IsAdmin|ReadOnly,)
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    search_fields = ('item__name', 'item__description')
    ordering_fields = ('item__rating', 'item__price')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return StockItem.objects.filter(amount__gt=0)

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAdmin,)

class CustomerDetailRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAdmin|IsOwner,)
    lookup_field = ('auth_id',)

class ReviewCommentListView(generics.ListCreateAPIView):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
    permission_classes = (IsAuthenticated|ReadOnly)

class TransactionStatusListView(generics.ListCreateAPIView):
    queryset = TransactionStatus.objects.all()
    serializer_class = TransactionStatusSerializer
    permission_classes = (IsAdmin|ReadOnly,)

class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAdmin,)
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    search_fields = ('customer__name', 'customer__email', 'transaction_items__item__name', 'transaction_items__item__description')
    filter_fields = ('status', )
    ordering_fields = ('status__status', 'datetime')

class TransactionDetailRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAdmin|IsOwner,)
