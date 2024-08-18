#watchlist_app/urls.py
from django.urls import path
from .views import CreateWatchlist
#api/v1/watchlist...
urlpatterns = [
    path('<str:watchlist_name>', CreateWatchlist.as_view())
]