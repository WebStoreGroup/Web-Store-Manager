from rest_framework import serializers
from .models import (
    Item,
    ItemCategory,
    ItemRating,
    PromoImage,
    StockItem,
    Customer,
    ReviewComment,
    TransactionStatus,
    Transaction,
    TransactionItem,
    Role
)

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'

class ItemRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRating
        fields = '__all__'

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category = ItemCategorySerializer()
    rating = ItemRatingSerializer()
    class Meta:
        model = Item
        fields = (
            'name',
            'category',
            'description',
            'price',
            'image',
            'rating',
            'review_comments',
        )

class PromoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoImage
        fields = (
            'id',
            'image',
        )

class StockItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = StockItem
        fields = (
            'id',
            'item',
            'amount',
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
            'phone_number',
            'transactions'
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
            'id',
            'item',
            'amount',
            'rating',
            'review_comment',
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
            'status',
            'confirmation_image',
        )

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'role',
        )