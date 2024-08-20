#portfolio_app/urls.py
from django.urls import path
from .views import Create_portfolio, Buy_pokemon, View_portfolio, Sell_pokemon

urlpatterns = [
    path('create/', Create_portfolio.as_view(), name='create_portfolio'),
    path('buy/', Buy_pokemon.as_view(), name='buy_pokemon'),
    path('sell/', Sell_pokemon.as_view(), name="sell_pokemon"),
    path('', View_portfolio.as_view(), name='view_portfolio')
]