#portfolio_app/urls.py
from django.urls import path
from .views import Create_portfolio

urlpatterns = [
    path('create/', Create_portfolio.as_view(), name='create_portfolio'),
]