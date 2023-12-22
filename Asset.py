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
        if type not in ["Stocks", "Real Estate", "Cryptocurrency", "Job"]:
            raise ValueError
        self._type = type

    @classmethod
    def get_asset_count(cls):
        return cls._asset_count  # Access class variable using classmethod

class Stock(Asset):
    def __init__(self, name, price, quantity):
        super().__init__("Stocks")
        self.name = name
        self.price = price
        self.quantity = quantity
