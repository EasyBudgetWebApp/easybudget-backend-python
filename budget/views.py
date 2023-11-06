from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

# Necessary imports for the API functionality
from rest_framework.decorators import api_view
from rest_framework.response import Response

from budget.forms import UserForm
from budget.models import CustomUser, Category, Recurrence, Transaction
from .serializers import CustomUserSerializer, CategorySerializer, TransactionSerializer, RecurrenceSerializer

# API views and functions
@api_view(['GET', 'POST', 'PUT'])
def getRoutes(request):
    # A list of available API endpoints
    listURLs = [
        'api/users/',
        'api/categories/',
        'api/recurrences/',
        'api/transactions/',
    ]
    return Response(listURLs)

@api_view(['GET'])
def getUsers(request):
    # Fetch all CustomUser instances
    ListCustomUser = CustomUser.objects.all()
    # Serialize the queryset
    serializer = CustomUserSerializer(ListCustomUser, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategories(request):
    # Fetch all Category instances
    ListCategories = Category.objects.all()
    # Serialize the queryset
    serializer = CategorySerializer(ListCategories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRecurrences(request):
    # Fetch all Recurrence instances
    ListRecurrences = Recurrence.objects.all()
    # Serialize the queryset
    serializer = RecurrenceSerializer(ListRecurrences, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTransactions(request):
    # Fetch all Transaction instances
    ListTransactions = Transaction.objects.all()
    # Serialize the queryset
    serializer = TransactionSerializer(ListTransactions, many=True)
    return Response(serializer.data)

# Existing views
class HomeTemplateView(TemplateView):
    template_name = 'homepage.html'

class CustomUserCreateView(CreateView):
    template_name = 'registration/create_user.html'
    model = CustomUser
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # If the form is valid, save the new user and set the name to title case
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.save()
            # Redirect to login page after successful user creation
            return redirect('login')
