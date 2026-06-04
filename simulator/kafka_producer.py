import json
import time
from kafka import KafkaProducer

from product_generator import generate_products
from customer_generator import generate_customers
from store_generator import generate_stores
from event_generator import generate_event

# Load master data
products_df = generate_products()
customers_df = generate_customers()
stores_df = generate_stores()

products = products_df.to_dict("records")
customers = customers_df.to_dict("records")
stores = stores_df.to_dict("records")

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TOPIC = "retail_events"

while True:
    event = generate_event(products, customers, stores)

    producer.send(TOPIC, event)

    print(event)

    time.sleep(1)