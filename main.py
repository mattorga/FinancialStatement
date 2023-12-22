from Asset import Asset, Stock

def main():
    stock1 = Stock("GOOG", 1200, 20)
    stock2 = Stock("AAPL", 150, 50)

    print("Total asset count:", Asset.get_asset_count())

if __name__ == "__main__":
    main()