from rest_framework import serializers
from .models import CustomUser, Recurrence, Transaction, Category

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff',
                  'is_active', 'date_joined', 'gender', 'date_of_birth', 'groups', 'user_permissions']


class RecurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurrence
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'