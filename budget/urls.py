from django.urls import path

from budget import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('create_user/', views.CustomUserCreateView.as_view(), name='create-user'),
]