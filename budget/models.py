import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    GENDER = (
        (1, "Man"),
        (2, "Woman"),
        (3, "Other"),
        (4, "Prefer not to say")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender = models.CharField(choices=GENDER)
    date_of_birth = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    type_of_income = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recurrence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    # ocurrence = models.
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2)
    # currency
    next_due_date = models.DateTimeField()


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    # currency = ?? List of currencies?
    transaction_date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recurrence = models.ForeignKey(Recurrence, on_delete=models.CASCADE, null=True, blank=True)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)  #It is impossible to add a non-nullable field 'custom_user' to transaction without specifying a default. Anyway all transactions will be always attrubuted to a user
