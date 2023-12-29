import pytest
from project import check_state, parseCrypto, parseStock
import requests
from bs4 import BeautifulSoup

def test_check_state():
    # Working
    assert check_state("1") == 1 
    assert check_state("2") == 2
    assert check_state("3") == 3 
    
    with pytest.raises(ValueError):
        check_state("asd")
        check_state("0")
        check_state("4")
        check_state(".!")

def test_parseStock():
    symbol, name, high, low, close, volume, url = parseStock('GOOGL')
    assert parseStock('GOOGL') == (symbol, name, high, low, close, volume, url)

    symbol, name, high, low, close, volume, url = parseStock('AAPL')
    assert parseStock('AAPL') == (symbol, name, high, low, close, volume, url)

    with pytest.raises(ValueError):
        parseStock("AXS")
        parseStock("ETH")
        parseStock("ASD")
        parseStock("123")

def test_parseCrypto(): 
    symbol, name,  high, low, close, circulating_supply, market_cap, coin_url = parseCrypto("AXS")
    assert parseCrypto("AXS") == (symbol, name,  high, low, close, circulating_supply, market_cap, coin_url)

    symbol, name,  high, low, close, circulating_supply, market_cap, coin_url = parseCrypto("ETH")
    assert parseCrypto("ETH") == (symbol, name,  high, low, close, circulating_supply, market_cap, coin_url)

    with pytest.raises(ValueError):
        parseCrypto("AAPL")
        parseCrypto("GOOGL")
        parseCrypto("123")
        parseCrypto("ASD")
    