from django.db import models
from user_app.models import App_user #importing this so we can make a portfolio be tied to a specific user. 
from pkmnstock_app.models import PkmnStock

# Create your models here.
class Portfolio(models.Model):
    user = models.OneToOneField(App_user, on_delete=models.CASCADE) #one user can only have one portfolio
    buying_power = models.DecimalField(default=20000.00, max_digits=12, decimal_places=2) #how much they start off
    total_portfolio = models.DecimalField(default=0, max_digits=12, decimal_places=2) #how much the user's portfolio is
    def __str__(self):
        return f"Portfolio of {self.user.username} - Total Value: ${self.total_portfolio}"
    
class PkmnPortfolio(models.Model): 
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='pkmn_in_portfolio') #to connect portfolio, which the portfolio can have many pokemon
    pokemon = models.ForeignKey(PkmnStock, on_delete=models.CASCADE, related_name='portfolio') #one portfolio can have many pkmn, we can grab the information of the pkmn thru here like price
    shares_purchased = models.IntegerField(default=1)  # number of shares purchased
    purchase_date = models.DateTimeField(auto_now_add=True)  # date of purchase
    total_price = models.DecimalField(max_digits=12, decimal_places=2)  # TOTAL price at which the shares were purchased

    def __str__(self):
        return f"{self.shares_purchased} shares of {self.pokemon.name} in {self.portfolio.user.username}'s portfolio"
    
