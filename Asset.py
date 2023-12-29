class Asset:
    _asset_count = 0
    _stocks_value = 0
    _crypto_value = 0
    _total_value = _stocks_value + _crypto_value

class Stock(Asset):
    def __init__(self, symbol, name, high, low, close, volume, url=0):
        self.type = "Stock"
        self.symbol = symbol
        self.name = name
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.volume = int(volume)
        self.url = url
        self.amount = int(0)
        Asset._asset_count += 1  # Increment asset count on object creation

    def buy(self, n):
        self.amount += float(n)
        value_bought = int(n) * float(self.close)
        Asset._stocks_value += value_bought
        Asset._total_value += value_bought
    def sell(self, n):
        if self.amount < n or not isinstance(n, int):
            raise ValueError()
        self.amount -= n
        value_sold = int(n * float(self.close))
        Asset._stocks_value -= value_sold
        Asset._total_value -= value_sold

    @property
    def amount(self):
        return int(self._amount)
    @amount.setter
    def amount(self, amount):
        self._amount = amount
    
    @property
    def value(self):
        return float(self._amount*self.close) 

class Cryptocurrency(Asset):
    def __init__(self, symbol, name, high, low, close, circulating_supply, market_cap, url="None"):
        self.type = "Cryptocurrency"
        self.symbol = symbol
        self.name = name
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.circulating_supply = int(circulating_supply)
        self.market_cap = float(market_cap)
        self.url = url
        self.amount = 0
        Asset._asset_count += 1  # Increment asset count on object creation

    def buy(self, n):
        self.amount += n
        value_bought = int(n * float(self.close))
        Asset._crypto_value += value_bought
        Asset._total_value += value_bought
    def sell(self, n):
        if self.amount < n:
            return "Invalid amounts to sell"
        self.amount -= n
        value_sold = int(n * float(self.close))
        Asset._crypto_value -= value_sold
        Asset._total_value -= value_sold
            
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, amount):
        self._amount = amount
    
    @property
    def value(self):
        value = int(self._amount*float(self.close))
        return value