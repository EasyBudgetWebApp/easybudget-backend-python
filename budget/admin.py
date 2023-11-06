from django.contrib import admin
from .models import CustomUser, Category, Recurrence, Transaction

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Recurrence)
admin.site.register(Transaction)
