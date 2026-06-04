import random
import pandas as pd

CITIES = [
    "New York", "Chicago", "Los Angeles", "Dallas",
    "Seattle", "Boston", "Miami", "Denver"
]

def generate_stores(n=20):
    stores = []

    for i in range(1, n + 1):
        stores.append({
            "store_id": f"S{i:03d}",
            "store_name": f"Retail Store {i}",
            "city": random.choice(CITIES)
        })

    return pd.DataFrame(stores)


if __name__ == "__main__":
    df = generate_stores()
    df.to_csv("../data/seeds/stores.csv", index=False)
    print("Stores generated:", len(df))