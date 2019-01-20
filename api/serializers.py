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
    item = ItemSerializer(read_only=True)
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
            'name',
            'email',
            'address',
            'phone_number'
        )

class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    status = TransactionStatusSerializer(read_only=True)
    class Meta:
        model = Transaction
        fields = (
            'customer',
            'datetime',
            'status'
        )

class TransactionItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    class Meta:
        model = TransactionItem
        fields = (
            'item'
            'amount'
        )