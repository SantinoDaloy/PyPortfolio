import datetime

# Supuestos: la cantidad que se tiene de una stock siempre ha sido la misma en el rango de fechas, 
# ya que de lo contrario, una stock debería tener un metodo ammount(date) que retorne cuantas stocks 
# se tenían en esa fecha
class Portfolio():
    def __init__(self, stocks: list):
        self.stocks = stocks

    def profit(self, start_date: datetime, end_date: datetime) -> float:
        portfolio_starting_value = 0
        portfolio_ending_value = 0
        period_in_years = (end_date - start_date).days / 365

        for stock in self.stocks:
            portfolio_starting_value += stock.Price(start_date)
            portfolio_ending_value += stock.Price(end_date)

        portfolio_profit = portfolio_ending_value - portfolio_starting_value
        annualized_return = ((portfolio_ending_value/portfolio_starting_value)**(1/period_in_years)) - 1
        
        return portfolio_profit, annualized_return