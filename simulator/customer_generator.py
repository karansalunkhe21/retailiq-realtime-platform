import random
import pandas as pd
from faker import Faker

fake = Faker()

SEGMENTS = ["Premium", "Regular", "Budget"]

def generate_customers(n=5000):
    customers = []

    for i in range(1, n + 1):

        segment = random.choices(
            SEGMENTS,
            weights=[0.1, 0.7, 0.2]
        )[0]

        customers.append({
            "customer_id": f"C{i:05d}",
            "name": fake.name(),
            "segment": segment,
            "city": fake.city(),
            "state": fake.state()
        })

    return pd.DataFrame(customers)


if __name__ == "__main__":
    df = generate_customers()
    df.to_csv("../data/seeds/customers.csv", index=False)
    print("Customers generated:", len(df))