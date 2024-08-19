from django.db import models
from user_app.models import App_user #importing this so we can make a watchlist be tied to a specific user. 
from pkmnstock_app.models import PkmnStock

class Watchlist(models.Model): 
    user = models.ForeignKey(App_user, on_delete=models.Model) #a user can have many watchlist, which the watchlist be tied to only one user
    name = models.CharField(max_length=30, unique=True) #to give the watchlist a name
    pokemon = models.ManyToManyField(PkmnStock, related_name='watchlist') #we will associate whatever pkmn the user adds to their watchlist
    #the related name establishes a reverse relationship to the model.

    def __str__(self): #this shows in django admin
        return f"  Watchlist : '{self.name}' ."
