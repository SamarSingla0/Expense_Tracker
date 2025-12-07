from django.urls import path, include
from . import views
from .views import ExpenseListView   # <-- This import is required

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/', ExpenseListView.as_view(), name='expense-list'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
