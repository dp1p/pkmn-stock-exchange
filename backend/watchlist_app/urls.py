#watchlist_app/urls.py
from django.urls import path
from .views import Create_watchlist, All_watchlist, Get_watchlist, Update_watchlist
#api/v1/watchlist...
urlpatterns = [
    path('create/', Create_watchlist.as_view(), name='create_watchlist'), #creating a watchlist
    path('all/', All_watchlist.as_view(), name='all_watchlist'), #reading all watchlist
    path('view/<str:watchlist_name>/', Get_watchlist.as_view(), name='get_watchlist'), #read a specfic watchlist
    path('update/<str:watchlist_name>/', Update_watchlist.as_view(), name='update_watchlist')
   
]