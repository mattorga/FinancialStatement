class Asset:
    _asset_count = 0 
    _total_value = 0

    @property
    def value(self):
        return Asset._total_value
    @property
    def asset_count(self):
        return Asset._asset_count  

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
    
    def buy(self, n):
        self.amount += n
        value_bought = int(n * float(self.close))
        Asset._total_value += value_bought
    def sell(self, n):
        if self.amount < n:
            return "Invalid amounts to sell"
        self.amount -= n
        value_sold = int(n * float(self.close))
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