from Asset import Asset, Stock
import requests
from bs4 import BeautifulSoup

def main():
    ticker = input("Ticker: ")
    _symbol, _name, _high, _low, _close, _volume, _url = parseStock(ticker)
    stock1 = Stock(_symbol, _name, _high, _low, _close, _volume, _url)

    print("Amount: ", stock1.amount)
    stock1.buy(10)
    print("Amount: ", stock1.amount)
    print("Value: ", stock1.value)
    stock1.sell(5)
    print("Amount: ", stock1.amount)
    print("Value: ", stock1.value)
    print(Asset._total_value)
    print(Asset._asset_count)
    
def parseStock(ticker):

    # Download webpage using requests
    home_url = f"http://eoddata.com/stocklist/NASDAQ/{ticker[0]}.htm"
    response = requests.get(home_url)
    # Retrieve the HTML document
    page_contents = response.text

    ## Parse the HTML code using BeautifulSoup library and extract the desired information
    doc = BeautifulSoup(page_contents, 'html.parser')

    tr_parent_ro = doc.find_all('tr',{'class':'ro'}) 
    tr_parent_re = doc.find_all('tr',{'class':'re'})

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
            return symbol, name, high, low, close, volume, url

    for j in range(len(tr_parent_re)):
        td_child_re = tr_parent_re[j].find_all('td') # Gets the necessary information
        symbol = td_child_re[0].find('a').text.strip()
        if symbol == ticker:
            name = td_child_re[1].text.strip()
            high = td_child_re[2].text.strip()
            low = td_child_re[3].text.strip()
            close = td_child_re[4].text.strip()
            volume = td_child_re[5].text.strip().replace(',', '') # Here we remove the comma
            url = "http://eoddata.com/" + td_child_re[0].find('a')['href'] # Here we append the base url
            return symbol, name, high, low, close, volume, url
                
    return "No ticker found"

if __name__ == "__main__":
    main()