from django.urls import path
from . import views

from .views import (
    PromoImageListView,
    ItemListView,
    ItemCategoryListView,
    CustomerListView,
    CustomerDetailRetrieveUpdateView,
    ReviewCommentListView,
    TransactionStatusListView,
    TransactionListView,
    TransactionDetailRetrieveUpdateView,
)

app_name = "api"

urlpatterns = [
    path('items/', ItemListView.as_view(), name="item_list"),
    path('promos/', PromoImageListView.as_view(), name="promo-list"),
    path('customers/', CustomerListView.as_view(), name="customer_list"),
    path('categories/', ItemCategoryListView.as_view(), name="category_list"),
    path('customers/<auth_id>/', CustomerDetailRetrieveUpdateView.as_view(), name="customer_detail"),
    path('reviews/', ReviewCommentListView.as_view(), name="review-list"),
    path('statuses/', TransactionStatusListView.as_view(), name="status_list"),
    path('transactions/', TransactionListView.as_view(), name="transaction_list"),
    path('transactions/<int:pk>/', TransactionDetailRetrieveUpdateView.as_view(), name="transaction_detail"),
]