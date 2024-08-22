#watchlist_app/urls.py
from django.urls import path
from .views import Create_watchlist, All_watchlist, Get_watchlist, Update_watchlist, Delete_from_watchlist, Delete_watchlist
#api/v1/watchlist...
urlpatterns = [
    path('create/', Create_watchlist.as_view(), name='create_watchlist'), #creating a watchlist
    path('', All_watchlist.as_view(), name='all_watchlist'), #reading all watchlist
    path('read/<str:watchlist_name>/', Get_watchlist.as_view(), name='get_watchlist'), #read a specfic watchlist
    path('update/<str:watchlist_name>/', Update_watchlist.as_view(), name='update_watchlist'), #update a watchlist
    path('delete/<str:watchlist_name>/', Delete_watchlist.as_view(), name="delete_watchlist"), #delete ENTIRE watchlist
    path('delete/<str:watchlist_name>/pkmn/', Delete_from_watchlist.as_view(), name='delete_from_watchlist') #delete pkmn FROM watchlist
]