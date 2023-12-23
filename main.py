from Asset import Asset, Stock
from datetime import date
import requests

def main():
    
    stockPrice("GOOGL")

def stockPrice(ticker):
    
    # Download webpage using requests
    home_url = 'http://eoddata.com/stocklist/TSX/A.htm'   #The URL Address of the webpage we will scrape, i.e. Stocks starting from A
    response = requests.get(home_url)
    print(response)


    # Parse the HTML code using BeautifulSoup library and extract the desired information

    # Building the scraper components

    # Compile the extracted information into a Python list and dictionaries

    # Converting the python dictionaries into Pandas Dataframes

    return ticker

if __name__ == "__main__":
    main()