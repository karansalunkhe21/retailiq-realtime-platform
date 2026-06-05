import sys
import os
import json
from kafka import KafkaConsumer
from datetime import datetime
import uuid

# Add project root to sys.path to allow running script directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from snowflake_conn.connection import get_connection

conn = get_connection()
cursor = conn.cursor()

consumer = KafkaConsumer(
    'product_views',
    'cart_events',
    'orders',
    'returns',
    'inventory_alerts',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🚀 Snowflake consumer started...")

for message in consumer:

    event = message.value
    topic = message.topic

    event_id = event.get("event_id", str(uuid.uuid4()))
    timestamp = event.get("timestamp", datetime.utcnow().isoformat())

    # -----------------------
    # ROUTING TO TABLES
    # -----------------------

    if topic == "product_views":
        cursor.execute("""
            INSERT INTO PRODUCT_VIEWS VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            event_id,
            event.get("event_type"),
            event.get("customer_id"),
            event.get("product_id"),
            event.get("store_id"),
            timestamp
        ))

    elif topic == "cart_events":
        cursor.execute("""
            INSERT INTO CART_EVENTS VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            event_id,
            event.get("event_type"),
            event.get("customer_id"),
            event.get("product_id"),
            event.get("store_id"),
            timestamp
        ))

    elif topic == "orders":
        cursor.execute("""
            INSERT INTO ORDERS VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            event_id,
            event.get("customer_id"),
            event.get("product_id"),
            event.get("store_id"),
            event.get("quantity"),
            event.get("price"),
            event.get("total_amount"),
            timestamp
        ))

    elif topic == "returns":
        cursor.execute("""
            INSERT INTO RETURNS VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            event_id,
            event.get("customer_id"),
            event.get("product_id"),
            event.get("store_id"),
            event.get("reason"),
            timestamp
        ))

    elif topic == "inventory_alerts":
        cursor.execute("""
            INSERT INTO INVENTORY_ALERTS VALUES (%s,%s,%s,%s)
        """, (
            event.get("event_type"),
            event.get("product_id"),
            event.get("remaining_qty"),
            timestamp
        ))

    conn.commit()

    print(f"Inserted from {topic}")