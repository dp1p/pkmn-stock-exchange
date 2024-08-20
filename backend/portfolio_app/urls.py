#portfolio_app/urls.py
from django.urls import path
from .views import Create_portfolio, Buy_portfolio, View_portfolio

urlpatterns = [
    path('create/', Create_portfolio.as_view(), name='create_portfolio'),
    path('buy/', Buy_portfolio.as_view(), name='buy_portfolio'),
    path('', View_portfolio.as_view(), name='view_portfolio')
]