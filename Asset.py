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
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.url = url
        self.amount = 0
        Asset._asset_count += 1  # Increment asset count on object creation
    
    def __str__(self):
        str = "Type: {}\nSymbol: {}\nName: {}\nHigh: ${}\nLow: ${}\nClose: ${}\nVolume: {}\nURL: {}".format(self.type, self.symbol, self.name, self.high, self.low, self.close, int(self.volume), self.url)
        return str

    def buy(self, n):
        self.amount += float(n)
        value_bought = int(n) * float(self.close)
        Asset._stocks_value += value_bought
        Asset._total_value += value_bought

    def sell(self, n):
        if self.amount < n:
            return "Invalid amounts to sell"
        self.amount -= n
        value_sold = int(n * float(self.close))
        Asset._stocks_value -= value_sold
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
        return f"${value}"

class Cryptocurrency(Asset):
    def __init__(self, symbol, name, open, high, low, close, circulating_supply, market_cap, url="None"):
        self.type = "Cryptocurrency"
        self.symbol = symbol
        self.name = name
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.circulating_supply = circulating_supply
        self.market_cap = market_cap
        self.url = url
        self.amount = 0
        Asset._asset_count += 1  # Increment asset count on object creation
    
    def __str__(self):
        str = "Type: {}\nSymbol: {}\nName: {}\nHigh: ${}\nLow: ${}\nClose: ${}\nCirculating Supply: {}\nMarket Cap: {}\nURL: {}".format(self.type, self.symbol, self.name, self.high, self.low, self.close, int(self.circulating_supply), int(self.market_cap), self.url)
        return str

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
        return f"${value}"