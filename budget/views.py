from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from budget.forms import UserForm
from budget.models import CustomUser


# Create your views here.
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