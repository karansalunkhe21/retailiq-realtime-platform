import json
import os
import sys
import uuid
from datetime import datetime

# Add project root to sys.path to allow imports of local packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kafka import KafkaConsumer
from snowflake.connection import get_connection

# Kafka Consumer
consumer = KafkaConsumer(
    "retail_events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

# Snowflake connection
conn = get_connection()
cursor = conn.cursor()

print("🚀 Consumer started... Listening to Kafka")

for message in consumer:

    event = message.value

    # Add metadata (VERY IMPORTANT in real systems)
    event_id = str(uuid.uuid4())
    ingested_at = datetime.utcnow()

    query = """
    INSERT INTO RETAILIQ.RAW.RETAIL_EVENTS (
        event_id,
        event_type,
        customer_id,
        product_id,
        store_id,
        quantity,
        price,
        total_amount,
        reason,
        event_timestamp,
        ingested_at
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(query, (
        event_id,
        event.get("event_type"),
        event.get("customer_id"),
        event.get("product_id"),
        event.get("store_id"),
        event.get("quantity"),
        event.get("price"),
        event.get("total_amount"),
        event.get("reason"),
        event.get("timestamp"),
        ingested_at
    ))

    conn.commit()

    print(f"✅ Inserted: {event['event_type']}")