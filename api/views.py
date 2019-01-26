from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Item,
    ItemCategory,
    PromoImage,
    StockItem,
    Customer,
    ReviewComment,
    TransactionStatus,
    Transaction,
    TransactionItem,
    Role
)
from .serializers import (
    ItemSerializer,
    ItemCategorySerializer,
    PromoImageSerializer,
    StockItemSerializer,
    CustomerSerializer,
    ReviewCommentSerializer,
    TransactionStatusSerializer,
    TransactionSerializer,
    RoleSerializer
)
from .permissions import (
    ReadOnly,
    IsAdmin,
    IsOwner,
    IsAuthenticated
)

# Create your views here.

class ItemCategoryListView(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    permission_classes = (IsAdmin|ReadOnly,)

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
    search_fields = ('item__name', 'item__description', 'item__category__category')
    filter_fields = ('item__category__category',)
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
    lookup_field = 'auth_id'

class ReviewCommentListView(generics.ListCreateAPIView):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
    permission_classes = (IsAdmin|IsAuthenticated|ReadOnly,)

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

class RoleListView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAdmin|ReadOnly,)