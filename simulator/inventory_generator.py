import pandas as pd
import random

products = pd.read_csv("data/seeds/products.csv")
stores = pd.read_csv("data/seeds/stores.csv")

inventory = []

for _, store in stores.iterrows():
    for _, product in products.iterrows():

        inventory.append({
            "store_id": store["store_id"],
            "product_id": product["product_id"],
            "inventory_qty": random.randint(50, 500)
        })

inventory_df = pd.DataFrame(inventory)

inventory_df.to_csv(
    "data/seeds/inventory.csv",
    index=False
)

print(f"Created {len(inventory_df)} inventory records")