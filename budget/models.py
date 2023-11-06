import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
GENDER = (
    ('man', 'Man'),
    ('woman', 'Woman'),
    ('other', 'Other'),
    ('nothing', 'Prefer not to say'),
)

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender = models.CharField(choices=GENDER, max_length=100)
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
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2)
    next_due_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recurrence = models.ForeignKey(Recurrence, on_delete=models.CASCADE, null=True, blank=True)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)  # Transactions will always be attributed to a user

    def __str__(self):
        return str(self.value)

