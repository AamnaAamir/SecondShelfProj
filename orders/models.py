from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# creates db table orders_order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


# creates db table orders_orderdetail
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.book.title} (x{self.quantity})"
