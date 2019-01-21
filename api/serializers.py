from rest_framework import serializers
from .models import (
    Item,
    StockItem,
    Customer,
    TransactionStatus,
    Transaction,
    TransactionItem
)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

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
