from Asset import Asset, Stock, Cryptocurrency
import sys
from scrapers import parseCrypto, parseStock
from tabulate import tabulate
from pyfiglet import Figlet

stocks_obj = []
crypto_obj = []

width = 132

# For tabulation purposes
stocks_dict = []
crypto_dict = []

def main():
    main_wallet()
        
def get_state():
    state = input("Action: ")
    return int(state)

def main_wallet():

    print("WALLET")
    print("Balance: ")
    print("1. Assets")
    print("2. Exit")

    wallet_state = get_state()

    match wallet_state:
        case 1:
            main_assets()
        case 2:
            sys.exit("Exiting...")
        
def main_assets():
    asset_state = 0

    print("ASSETS")
    print(f"Value: ${Asset._total_value}")
    print("1. Stocks")
    print("2. Cryptocurrency")
    print("3. View All")
    print("4. Back")

    asset_state = get_state()

    match asset_state:
        case 1:
            sub_stocks()
        case 2:
            sub_crypto()
        case 3:
            asset_view_all()
        case 4:
            main_wallet()

def asset_view_all():
    ...

def sub_stocks():
    
    print("+" + "-"*width + "+")
    print("|" + " "*63 + "STOCKS" + " "*63 + "|")
    
    if stocks_obj:
        print(tabulate(stocks_dict, headers="keys", tablefmt="grid", numalign="center"))
        str = f"Total Value: ${Asset._stocks_value}"
        pad = int(len(str)/2)
        print("|" + " "*(66-pad) + f"{str}" + " "*(66-pad) + "|")
    print("+" + "-"*width + "+")

    print("1. Buy")
    print("2. Sell")
    print("3. Back")

    stock_state = get_state()

    match stock_state:
        case 1: # Buy
            ticker = input("Ticker: ")

            # Check for existing stocks
            for stock in stocks_obj:
                if stock.symbol == ticker:
                    print(stock)
                    amount = int(input("Amount: "))
                    stock.buy(amount)
                    for index in stocks_dict:
                        if index["Symbol"] == ticker:
                            index.update({"Quantity":stock.amount, "Value":stock.value})
                            sub_stocks()

            # Create a new stock
            symbol, name, high, low, close, volume, url = parseStock(ticker)
            stock = Stock(symbol, name, high, low, close, volume, url)
            print(stock)
            amount = int(input("Amount: "))
            stock.buy(amount)
            stocks_obj.append(stock)
            stocks_dict.append({"Symbol": stock.symbol, "Name":stock.name, "High": stock.high, "Low":stock.low, "Close":stock.close, "Volume":stock.volume, "Quantity":stock.amount, "Value":stock.value, "URL":stock.url})
            sub_stocks()

        case 2: #Sell
            ticker = input("Ticker: ")
            # Check for existing stocks
            for stock in stocks_obj:
                if stock.symbol == ticker:
                    amount = int(input("Amount: "))
                    stock.sell(amount)
                    for index in stocks_dict:
                        if index["Symbol"] == ticker:
                            index.update({"Quantity":stock.amount, "Value":stock.value})
                            sub_stocks()
            
            print("You have no such stock...")
            sub_stocks()
        case 3:
            main_assets()

def sub_crypto():
    
    print("+" + "-"*width + "+")
    print("|" + " "*59 + "CRYPTOCURRENCY" + " "*59 + "|")
    
    if crypto_obj:
        print(tabulate(crypto_dict, headers="keys", tablefmt="grid", numalign="center"))
        str = f"Total Value: ${Asset._crypto_value}"
        pad = int(len(str)/2)
        print("|" + " "*(66-pad) + f"{str}" + " "*(66-pad) + "|")
    print("+" + "-"*width + "+")

    print("1. Buy")
    print("2. Sell")
    print("3. Back")

    crypto_state = get_state()

    match crypto_state:
        case 1: # Buy
            ticker = input("Ticker: ")

            # Check for existing stocks
            for crypto in crypto_obj:
                if crypto.symbol == ticker:
                    print(crypto)
                    amount = int(input("Amount: "))
                    crypto.buy(amount)
                    for index in crypto_dict:
                        if index["Symbol"] == ticker:
                            index.update({"Quantity":crypto.amount, "Value":crypto.value})
                            sub_stocks()

            # Create a new stock
            symbol, name, open, high, low, close, circulating_supply, market_cap, coin_url = parseCrypto(ticker)
            crypto = Cryptocurrency(symbol, name, open, high, low, close, circulating_supply, market_cap, coin_url)
            print(crypto)
            amount = int(input("Amount: "))
            crypto.buy(amount)
            crypto_obj.append(crypto)
            crypto_dict.append({"Symbol": crypto.symbol, "Name":crypto.name, "High": crypto.high, "Low":crypto.low, "Close":crypto.close, "Volume":int(crypto.circulating_supply), "Quantity":crypto.amount, "Value":crypto.value, "URL":crypto.url})
            sub_crypto()

        case 2: #Sell
            ticker = input("Ticker: ")
            # Check for existing cryptocurrency
            for crypto in crypto_obj:
                if crypto.symbol == ticker:
                    amount = int(input("Amount: "))
                    crypto.sell(amount)
                    for index in crypto_dict:
                        if index["Symbol"] == ticker:
                            index.update({"Quantity":crypto.amount, "Value":crypto.value})
                            sub_crypto()
            
            print("You have no such stock...")
            sub_crypto()
        case 3:
            main_assets()
    
if __name__ == "__main__":
    main()