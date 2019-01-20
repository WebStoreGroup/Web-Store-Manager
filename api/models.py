from django.db import models
from django.core.validators import RegexValidator
from djmoney.models.fields import MoneyField

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = MoneyField(decimal_places=2, default=0, default_currency='IDR', max_digits=13,)

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name

class StockItem(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Stock Items"

    def __str__(self):
        return "{} ({})".format(self.item, self.amount) 

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    class Meta:
        verbose_name_plural = "Customers"
    
    def __str__(self):
        return "{} - {}".format(self.id, self.name)

class TransactionStatus(models.Model):
    status = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Transaction Statuses"

    def __str__(self):
        return self.status

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="transactions")
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Transactions"

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total
    
    def __str__(self):
        return "Transaction {} - {}".format(self.id, self.customer)

class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="items")
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = "Transaction Items"

    def __str__(self):
        return "{} / {} ({})".format(self.transaction, self.item, self.amount)