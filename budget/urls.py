from django.urls import path

from budget import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('create_user/', views.CustomUserCreateView.as_view(), name='create-user'),
    path('api/', views.getRoutes, name='api-routes'),
    path('api/users/', views.getUsers, name='api-users'),
    path('api/categories/', views.getCategories, name='api-categories'),
    path('api/recurrences/', views.getRecurrences, name='api-recurrences'),
    path('api/transactions/', views.getTransactions, name='api-transactions'),
]
