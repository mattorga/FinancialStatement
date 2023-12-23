class Asset:
    _asset_count = 0  # Class variable to track asset count

    def __init__(self, type):
        self.type = type
        Asset._asset_count += 1  # Increment asset count on object creation

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type not in ["Stock", "Real Estate", "Cryptocurrency", "Job"]:
            raise ValueError
        self._type = type

    @classmethod # To get a class variable at Line 2
    def get_asset_count(cls):
        return cls._asset_count  # Access class variable using classmethod

class Stock(Asset):
    def __init__(self, name, price, quantity):
        super().__init__("Stock")
        self.name = name
        self.price = price
        self.quantity = quantity

#stock1 = Stock("GOOG", 15, 20)
#stock2 = Stock("AAPL", 150, 50)
#print("Total asset count:", Asset.get_asset_count())