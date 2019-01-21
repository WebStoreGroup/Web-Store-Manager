from django.urls import path
from . import views

from .views import (
    ItemListView,
    StockItemListView,
    CustomerListView,
    TransactionStatusListView,
    TransactionListView,
    TransactionDetailRetrieveView,
)

app_name = "api"

urlpatterns = [
    path('items/', ItemListView.as_view(), name="item_list"),
    path('stock-items/', StockItemListView.as_view(), name="stock_item_list"),
    path('customers/', CustomerListView.as_view(), name="customer_list"),
    path('statuses/', TransactionStatusListView.as_view(), name="status_list"),
    path('transactions/', TransactionListView.as_view(), name="transaction_list"),
    path('transactions/<int:pk>/', TransactionDetailRetrieveView.as_view(), name="transaction_detail"),
]