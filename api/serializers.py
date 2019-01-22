from rest_framework import serializers
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

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    review_comments = ReviewCommentSerializer(many=True)
    class Meta:
        model = Item
        fields = (
            'name',
            'description',
            'price',
            'image',
            'rating',
            'review_comments'
        )

class PromoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoImage
        fields = (
            'image',
        )

class StockItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = StockItem
        fields = (
            'item',
            'amount'
        )

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'name',
            'email',
            'auth_id',
            'address',
            'phone_number'
        )

class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = '__all__'

class TransactionItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = TransactionItem
        fields = (
            'item',
            'amount',
        )

class TransactionSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    status = TransactionStatusSerializer()
    transaction_items = TransactionItemSerializer(many=True)
    class Meta:
        model = Transaction
        fields = (
            'id',
            'customer',
            'transaction_items',
            'datetime',
            'status'
        )
