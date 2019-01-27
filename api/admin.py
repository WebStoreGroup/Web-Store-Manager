from django.contrib import admin
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

# Register your models here.

admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(ItemRating)
admin.site.register(PromoImage)
admin.site.register(StockItem)
admin.site.register(Customer)
admin.site.register(ReviewComment)
admin.site.register(TransactionStatus)
admin.site.register(Transaction)
admin.site.register(TransactionItem)
admin.site.register(Role)