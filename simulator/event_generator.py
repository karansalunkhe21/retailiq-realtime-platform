import random
import time
from datetime import datetime
from config import EVENT_WEIGHTS

def choose_event():
    events = list(EVENT_WEIGHTS.keys())
    weights = list(EVENT_WEIGHTS.values())
    return random.choices(events, weights=weights)[0]


def generate_event(products, customers, stores):

    event_type = choose_event()

    customer = random.choice(customers)
    product = random.choice(products)
    store = random.choice(stores)

    base_event = {
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "customer_id": customer["customer_id"],
        "product_id": product["product_id"],
        "store_id": store["store_id"]
    }

    # enrich based on event type
    if event_type == "order":
        base_event["quantity"] = random.randint(1, 3)
        base_event["price"] = product["price"]
        base_event["total_amount"] = round(base_event["quantity"] * product["price"], 2)

    elif event_type == "add_to_cart":
        base_event["quantity"] = 1

    elif event_type == "return":
        base_event["reason"] = random.choice([
            "damaged", "wrong item", "not needed", "late delivery"
        ])

    return base_event