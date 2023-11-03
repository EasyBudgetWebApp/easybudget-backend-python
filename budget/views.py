from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from budget.forms import UserForm
from budget.models import CustomUser, Category, Recurrence, Transaction

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer, CategorySerializer, TransactionSerializer, RecurrenceSerializer


class HomeTemplateView(TemplateView):
    template_name = 'homepage.html'

class CustomUserCreateView(CreateView):
    template_name = 'registration/create_user.html'
    model = CustomUser
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name=new_user.last_name.title()
            new_user.save()
        return redirect('login')


@api_view(['GET', 'POST', 'PUT'])
def getRoutes(request):
    listURLS = [
        'api/users/',
        'api/categories/',
        'api/recurrences/',
        'api/transactions/',
    ]
    return Response(listURLS)

@api_view(['GET'])
def getUsers(request):
    ListCustomUser = CustomUser.objects.all()
    serializer = CustomUserSerializer(ListCustomUser, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategories(request):
    ListCategories = Category.objects.all()
    serializer = CategorySerializer(ListCategories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRecurrences(request):
    ListRecurrences = Recurrence.objects.all()
    serializer = RecurrenceSerializer(ListRecurrences, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTransactions(request):
    ListTransactions = Transaction.objects.all()
    serializer = TransactionSerializer(ListTransactions, many=True)
    return Response(serializer.data)
