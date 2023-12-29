from Asset import Asset, Stock, Cryptocurrency
import sys
from scrapers import parseCrypto, parseStock
from tabulate import tabulate
from prettytable import PrettyTable 
import time

stocks_obj = []
crypto_obj = []

def main():
    main_assets()
        
def get_state():
   while True:
        choice = int(input("Action: "))
        try:
            if  choice > 3:
                raise ValueError()
            else:
                return choice
        except (ValueError):
            pass
            
def main_assets():
    asset_state = 0

    print("="*160)

    table_display = PrettyTable()
    if stocks_obj or crypto_obj:
        table_display.title = F"ASSETS (${Asset._total_value:.2f})"
        table_display.field_names = ["Type", "Name", "Symbol", "High", "Low", "Close", "Volume", "Quantity", "Value", "URL"]
        for stock in stocks_obj:
            table_display.add_row([stock.type, stock.name, stock.symbol, f"${stock.high}", f"${stock.low}", f"${stock.close}", stock.volume, stock.amount, f"${stock.value:.2f}", stock.url])
        for crypto in crypto_obj:
            table_display.add_row([crypto.type, crypto.name, crypto.symbol, f"${crypto.high:.2f}", f"${crypto.low:.2f}", f"${crypto.close:.2f}", crypto.circulating_supply, crypto.amount, f"${crypto.value:.2f}", crypto.url])
        table_display.sortby = "Type"
        print(table_display)
    else:
        table_display.add_row(["No Assets"])
        table_display.header = False
        print(table_display)

    print("1. Stocks")
    print("2. Cryptocurrency")
    print("3. Back")

    asset_state = get_state()

    match asset_state:
        case 1:
            sub_stocks()
        case 2:
            sub_crypto()
        case 3:
            print("Exiting...")
            time.sleep(2)
            sys.exit()

def sub_stocks():
    print("="*160)

    table_display = PrettyTable()
    if stocks_obj:
        table_display.title = F"STOCKS (${Asset._stocks_value:.2f})"
        table_display.field_names = ["Name", "Symbol", "High", "Low", "Close", "Volume", "Quantity", "Value", "URL"]
        for stock in stocks_obj:
            table_display.add_row([stock.name, stock.symbol, f"${stock.high}", f"${stock.low}", f"${stock.close}", stock.volume, stock.amount, f"${stock.value:.2f}", stock.url])
        print(table_display)

    else:
        table_display.add_row(["No Stocks"])
        table_display.header = False
        print(table_display)

    print("1. Buy")
    print("2. Sell")
    print("3. Back")

    stock_state = get_state()
    table = PrettyTable() 
    match stock_state:
        case 1: # Buy
            ticker = input("Ticker: ")
            for stock in stocks_obj:
                if stock.symbol == ticker: # Stock exists
                    table.title = stock.name
                    table.field_names = ["Symbol", "High", "Low", "Close", "Volume", "Quantity", "Value","URL"]
                    table.add_row([stock.symbol, f"{stock.high}", f"{stock.low}", f"{stock.close}", stock.volume, stock.amount, f"{stock.value}", stock.url])
                    print(table)

                    amount = -1
                    while amount < 0:
                        amount = int(input("Amount: "))
                    if amount != 0:
                        stock.buy(amount)
                    sub_stocks()

            # Creates a new stock
            try:
                symbol, name, high, low, close, volume, url = parseStock(ticker)
                stock = Stock(symbol, name, high, low, close, volume, url)
                table.title = stock.name
                table.field_names = ["Symbol", "High", "Low", "Close", "Volume", "URL"]
                table.add_row([stock.symbol, f"{stock.high}", f"{stock.low}", f"{stock.close}", stock.volume, stock.url])
                print(table)

                amount = -1
                while amount < 0:
                    amount = int(input("Amount: "))
                if amount != 0:
                    stocks_obj.append(stock)
                    stock.buy(amount)
            except:
                print(f"Found no stock with ticker, '{ticker}'.")
                time.sleep(1)
        
            sub_stocks()
                
        case 2: #Sell
            found = False
            if stocks_obj:
                ticker = input("Ticker: ")
                for stock in stocks_obj:
                    if stock.symbol == ticker: # Stock exists
                        found = True
                        table.title = stock.name
                        table.field_names = ["Symbol", "High", "Low", "Close", "Volume", "Quantity", "Value","URL"]
                        table.add_row([stock.symbol, f"{stock.high}", f"{stock.low}", f"{stock.close}", stock.volume, stock.amount, f"{stock.value}", stock.url])
                        print(table)

                        amount = -1
                        while amount < 0:
                            amount = int(input("Amount: "))
                        if amount != 0:
                            try:
                                stock.sell(amount)
                                if stock.amount == 0:
                                    stocks_obj.remove(stock)
                            except:
                                print("Invalid amount to sell...")
                                time.sleep(1)
                        
            if not found:
                print(f"You have no such stock.")
                time.sleep(1)

            sub_stocks()

        case 3:
            main_assets()

def sub_crypto():
    print("="*160)

    table_display = PrettyTable()
    if crypto_obj:
        table_display.title = f"CRYPTOCURRENCY (${Asset._crypto_value:.2f})"
        table_display.field_names = ["Name", "Symbol", "High", "Low", "Close", "Supply", "Market Cap", "Quantity", "Value", "URL"]
        for crypto in crypto_obj:
            table_display.add_row([crypto.name, crypto.symbol, f"${crypto.high:.2f}", f"${crypto.low:.2f}", f"${crypto.close:.2f}", crypto.circulating_supply, f"${crypto.market_cap:.2f}", crypto.amount, f"${crypto.value:.2f}", crypto.url])
        print(table_display)

    else:
        table_display.add_row(["No Cryptocurrencies"])
        table_display.header = False
        print(table_display)

    print("1. Buy")
    print("2. Sell")
    print("3. Back")

    crypto_state = get_state()
    table = PrettyTable() 
    match crypto_state:
        case 1: # Buy
            ticker = input("Ticker: ")
            for crypto in crypto_obj:
                if crypto.symbol == ticker: # Stock exists
                    table.title = crypto.name
                    table.field_names = ["Symbol", "High", "Low", "Close", "Circulating Supply", "Market Cap", "Quantity", "Value","URL"]
                    table.add_row([crypto.symbol, f"{crypto.high:.2f}", f"{crypto.low:.2f}", f"{crypto.close:.2f}", crypto.circulating_supply, f"{crypto.market_cap:.2f}",f"{crypto.amount}", f"{crypto.value:.2f}", crypto.url])
                    print(table)

                    amount = -1
                    while amount < 0:
                        amount = int(input("Amount: "))
                    if amount != 0:
                        crypto.buy(amount)
                    sub_crypto()

            # Creates a new stock

            symbol, name,  high, low, close, circulating_supply, market_cap, coin_url = parseCrypto(ticker)
            crypto = Cryptocurrency(symbol, name,  high, low, close, circulating_supply, market_cap, coin_url)
            table.title = crypto.name
            table.field_names = ["Symbol", "High", "Low", "Close", "Circulating Supply", "Market Cap", "URL"]
            table.add_row([crypto.symbol, f"${crypto.high:.2f}", f"${crypto.low:.2f}", f"${crypto.close:.2f}", crypto.circulating_supply, f"${crypto.market_cap:.2f}", crypto.url])
            print(table)

            amount = -1
            while amount < 0:
                amount = int(input("Amount: "))
            if amount != 0:
                crypto_obj.append(crypto)
                crypto.buy(amount)
            
                #print(f"Found no crypto with ticker, '{ticker}'.")
                #time.sleep(1)
        
            sub_crypto()
                
        case 2: #Sell
            found = False
            if crypto_obj:
                ticker = input("Ticker: ")
                for crypto in crypto_obj:
                    if crypto.symbol == ticker: # Stock exists
                        table.title = crypto.name
                        table.field_names = ["Symbol", "High", "Low", "Close", "Circulating Supply", "Market Cap", "Quantity", "Value", "URL"]
                        table.add_row([crypto.symbol, f"{crypto.high:.2f}", f"{crypto.low:.2f}", f"{crypto.close:.2f}", crypto.circulating_supply, f"{crypto.market_cap:.2f}",f"{crypto.amount}", f"{crypto.value:.2f}", crypto.url])
                        print(table)
                        found = True

                        amount = -1
                        while amount < 0:
                            amount = int(input("Amount: "))
                        if amount != 0:
                            try:
                                crypto.sell(amount)
                                if crypto.amount == 0:
                                    crypto_obj.remove(crypto)
                            except:
                                print("Invalid amount to sell...")
                                time.sleep(1)
                        
            if not found:
                print(f"You have no such crypto.")
                time.sleep(1)

            sub_crypto()

        case 3:
            main_assets()

if __name__ == "__main__":
    main()