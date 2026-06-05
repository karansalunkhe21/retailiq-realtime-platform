import json
import time
import random
import pandas as pd
from datetime import datetime
from kafka import KafkaProducer

# ----------------------------
# LOAD MASTER DATA
# ----------------------------
products = pd.read_csv("data/seeds/products.csv")
customers = pd.read_csv("data/seeds/customers.csv")
stores = pd.read_csv("data/seeds/stores.csv")
inventory = pd.read_csv("data/seeds/inventory.csv")

# ----------------------------
# PRODUCT POPULARITY (ZIPF-LIKE)
# ----------------------------
products = products.sample(frac=1).reset_index(drop=True)
products["weight"] = [1 / (i + 1) for i in range(len(products))]
products["weight"] = products["weight"] / products["weight"].sum()

product_list = products.to_dict("records")
customer_list = customers.to_dict("records")
store_list = stores.to_dict("records")

# inventory state (in-memory)
inventory_map = inventory.set_index("product_id")["inventory_qty"].to_dict()

# ----------------------------
# KAFKA PRODUCER
# ----------------------------
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# ----------------------------
# EVENT ROUTER
# ----------------------------
def route_event(event_type):
    if event_type == "view":
        return "product_views"
    elif event_type == "cart":
        return "cart_events"
    elif event_type == "order":
        return "orders"
    elif event_type == "return":
        return "returns"
    else:
        return "retail_events"


# ----------------------------
# EVENT GENERATOR
# ----------------------------
def generate_event():

    customer = random.choice(customer_list)
    store = random.choice(store_list)

    product = random.choices(
        product_list,
        weights=products["weight"].values,
        k=1
    )[0]

    event_type = random.choices(
        ["view", "cart", "order", "return"],
        weights=[70, 20, 8, 2]
    )[0]

    event = {
        "event_id": str(random.randint(100000, 999999)),
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "customer_id": customer["customer_id"],
        "product_id": product["product_id"],
        "store_id": store["store_id"]
    }

    # ----------------------------
    # ORDER LOGIC
    # ----------------------------
    if event_type == "order":

        quantity = random.randint(1, 3)

        event["quantity"] = quantity
        event["price"] = product["price"]
        event["total_amount"] = round(quantity * product["price"], 2)

        # update inventory
        pid = product["product_id"]
        if pid in inventory_map:
            inventory_map[pid] -= quantity

    # ----------------------------
    # RETURN LOGIC
    # ----------------------------
    if event_type == "return":
        event["reason"] = random.choice([
            "damaged",
            "wrong item",
            "not needed",
            "late delivery"
        ])

    # ----------------------------
    # LOW STOCK EVENT
    # ----------------------------
    pid = product["product_id"]
    if pid in inventory_map and inventory_map[pid] < 20:

        producer.send("inventory_alerts", {
            "event_type": "low_stock",
            "product_id": pid,
            "remaining_qty": inventory_map[pid],
            "timestamp": datetime.utcnow().isoformat()
        })

    return event


# ----------------------------
# STREAMING LOOP
# ----------------------------
print("🚀 Multi-topic retail simulator running...")

while True:

    event = generate_event()

    topic = route_event(event["event_type"])

    producer.send(topic, event)

    print(f"Sent to {topic}: {event}")

    time.sleep(1)