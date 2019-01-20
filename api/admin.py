from django.contrib import admin
from .models import (
    Item,
    StockItem,
    Customer,
    TransactionStatus,
    Transaction,
    TransactionItem
)

# Register your models here.

admin.site.register(Item)
admin.site.register(StockItem)
admin.site.register(Customer)
admin.site.register(TransactionStatus)
admin.site.register(Transaction)
admin.site.register(TransactionItem)