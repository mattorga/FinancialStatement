from Asset import Asset, Stock, Cryptocurrency
import sys
try: 
    from prettytable import PrettyTable
except:
    pass

import time
import requests
from bs4 import BeautifulSoup

stocks_obj = []
crypto_obj = []

def main():
    main_assets()
        
def check_state(choice):
    try: 
        choice = int(choice)
        if  choice < 1 or choice > 3:
            raise ValueError()
        else:
            return choice
    except ValueError:
        print("Out-of-range or non-number input...")
        time.sleep(1)
        raise
   
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

    while True:
        choice = input("Action: ")
        try:
            asset_state = check_state(choice)
            break
        except (ValueError, TypeError):
            pass
    

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

    while True:
        choice = input("Action: ")
        try:
            stock_state = check_state(choice)
            break
        except (ValueError, TypeError):
            pass
    
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
            except:
                print(f"Found no stock with ticker, '{ticker}'.")
                time.sleep(1)
                sub_stocks()

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

    while True:
        choice = input("Action: ")
        try:
            crypto_state = check_state(choice)
            break
        except (ValueError, TypeError):
            pass

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

            try:
                symbol, name,  high, low, close, circulating_supply, market_cap, coin_url = parseCrypto(ticker)
            except:
                print(f"Found no crypto with ticker, '{ticker}'")
                time.sleep(1)
                sub_crypto()
            
            crypto = Cryptocurrency(symbol, name,  high, low, close, circulating_supply, market_cap, coin_url)
            table.title = crypto.name
            table.field_names = ["Symbol", "High", "Low", "Close", "Circulating Supply", "Market Cap", "URL"]
            table.add_row([crypto.symbol, f"${crypto.high:.2f}", f"${crypto.low:.2f}", f"${crypto.close:.2f}", crypto.circulating_supply, f"${crypto.market_cap:.2f}", crypto.url])
            print(symbol, name,  high, low, close, circulating_supply, market_cap, coin_url)
            print(table)

            amount = -1
            while amount < 0:
                amount = int(input("Amount: "))
            if amount != 0:
                crypto_obj.append(crypto)
                crypto.buy(amount)
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

def parseStock(ticker):
    ticker = ticker.upper()
    # Download webpage using requests
    URL = f"http://eoddata.com/stocklist/NASDAQ/{ticker[0]}.htm"

    response = requests.get(URL)
    # Retrieve the HTML document
    page_contents = response.text

    ## Parse the HTML code using BeautifulSoup library and extract the desired information
    doc = BeautifulSoup(page_contents, 'html.parser')
    
    tr_parent_ro = doc.find_all('tr',{'class':'ro'}) 
    tr_parent_re = doc.find_all('tr',{'class':'re'})

    found = False
    for i in range(len(tr_parent_ro)): # Search ro class
        td_child_ro = tr_parent_ro[i].find_all('td') # Gets the necessary information
        symbol = td_child_ro[0].find('a').text.strip()
        if symbol == ticker:
            name = td_child_ro[1].text.strip()
            high = td_child_ro[2].text.strip()
            low = td_child_ro[3].text.strip()
            close = td_child_ro[4].text.strip()
            volume = td_child_ro[5].text.strip().replace(',', '') # Here we remove the comma
            url = "http://eoddata.com/" + td_child_ro[0].find('a')['href'] # Here we append the base url
            print(symbol, name, high, low, close, volume, url)
            found = True

    for j in range(len(tr_parent_re)):
        td_child_re = tr_parent_re[j].find_all('td') # Gets the necessary information
        symbol = td_child_re[0].find('a').text.strip()
        if symbol == ticker and found == False:
            name = td_child_re[1].text.strip()
            high = td_child_re[2].text.strip()
            low = td_child_re[3].text.strip()
            close = td_child_re[4].text.strip()
            volume = td_child_re[5].text.strip().replace(',', '') # Here we remove the comma
            url = "http://eoddata.com/" + td_child_re[0].find('a')['href'] # Here we append the base url
            print(symbol, name, high, low, close, volume, url)
            found = True
    
    if found:
        return ticker, name, high, low, close, volume, url
    else:
        raise ValueError()
        
def parseCrypto(ticker):
    ticker = ticker.upper()
    URL = f"https://production.api.coindesk.com/v2/tb/price/ticker?assets={ticker}"
    response = requests.get(URL)
    
        
    json_data = response.json()
    found = True
    try:
        coin_data = json_data['data'][ticker]
    except:
        found = False
            
    if found:
        symbol = coin_data['iso'],
        name = coin_data['name'],
        open = coin_data['ohlc']['o']
        high = coin_data['ohlc']['h']
        low = coin_data['ohlc']['l']
        close = coin_data['ohlc']['c']
        circulating_supply = coin_data['circulatingSupply']
        market_cap = coin_data['marketCap']
        
        coin_url = f"https://www.coindesk.com/price/{name[0].lower().replace(' ', '-')}/"

        return symbol[0], name[0], high, low, close, circulating_supply, market_cap, coin_url
    else:
        raise ValueError()

if __name__ == "__main__":
    main()