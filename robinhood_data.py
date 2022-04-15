import robin_stocks.robinhood as R
from os import environ


class RobinhoodData:
    def __init__(self):
        # robinhood_user_name and robinhood_password are two variables saved as environmental variable.
        self.login = R.login(environ.get('robinhood_user_name'), environ.get('robinhood_password'))
        self.my_stocks = {}

        # R.logout()

    def get_stock_data(self):
        # A dictionary that's gonna store all my stock info
        self.my_stocks = R.build_holdings()
