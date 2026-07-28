from client import PriceTrackerClient

def main():
    client = PriceTrackerClient()
    res = client.track_price(product='SKU-101', competitor_url='http://comp.com/item')
    print(f"Result for price_diff_pct: {res['price_diff_pct']}")

if __name__ == "__main__":
    main()
