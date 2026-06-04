import random
import pandas as pd

CATEGORIES = {
    "Electronics": ["Laptop", "Phone", "Tablet", "Camera"],
    "Accessories": ["Headphones", "Mouse", "Keyboard", "Charger"],
    "Home": ["Blender", "Microwave", "Vacuum", "Air Fryer"],
    "Gaming": ["Console", "Controller", "Game"],
}

BRANDS = ["Apple", "Samsung", "Sony", "Dell", "HP", "LG", "Bose"]

def generate_products(n=500):
    products = []

    for i in range(1, n + 1):
        category = random.choice(list(CATEGORIES.keys()))
        base_product = random.choice(CATEGORIES[category])
        brand = random.choice(BRANDS)

        price = round(random.uniform(20, 2000), 2)

        products.append({
            "product_id": f"P{i:04d}",
            "product_name": f"{brand} {base_product}",
            "category": category,
            "brand": brand,
            "price": price
        })

    return pd.DataFrame(products)


if __name__ == "__main__":
    df = generate_products()
    df.to_csv("../data/seeds/products.csv", index=False)
    print("Products generated:", len(df))