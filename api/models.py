from django.db import models
from django.core.validators import RegexValidator
from djmoney.models.fields import MoneyField

# Create your models here.

class ItemCategory(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, related_name="items", default=3)
    description = models.CharField(max_length=300)
    price = MoneyField(decimal_places=2, default=0, default_currency='IDR', max_digits=13)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name

class ItemRating(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name="rating")
    rating = models.FloatField(default=0.0)
    rater_number = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Item Ratings"

    def __str__(self):
        return "Rating of {} : {}".format(self.item, self.rating)

    def update_rating(self, new_rating):
        self.rating = (self.rating * self.rater_number + new_rating) / (self.rater_number + 1)
        self.rater_number += 1

class PromoImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Promo Images"

    def __str__(self):
        return "{} - {}".format(self.title, self.datetime)

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
    auth_id = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Customers"
    
    def __str__(self):
        return "{} - {}".format(self.id, self.name)

class ReviewComment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="review_comments")
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL, related_name="buyers")
    comment = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Review Comments"

    def __str__(self):
        return "Comment ({}) - {} - {}".format(self.id, self.item, self.customer)

class TransactionStatus(models.Model):
    status = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Transaction Statuses"

    def __str__(self):
        return self.status

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="transactions")
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(TransactionStatus, on_delete=models.CASCADE, related_name="transactions", default=1)
    confirmation_image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Transactions"

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total
    
    def __str__(self):
        return "[{}] Transaction {} / {}".format(self.status, self.id, self.customer)

class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="transaction_items")
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    rating = models.FloatField(blank=True, null=True)
    review_comment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Transaction Items"

    def __str__(self):
        return "{} / {} ({})".format(self.transaction, self.item, self.amount)

class Role(models.Model):
    ROLES_CHOICE = (
        ('CUSTOMER', 'Customer'),
        ('ADMIN', 'Admin')
    )
    role = models.CharField(choices=ROLES_CHOICE, max_length=100)

    class Meta:
        verbose_name_plural = "Roles"
    
    def __str__(self):
        return self.role