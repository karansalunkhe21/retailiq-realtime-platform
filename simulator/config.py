# simulator/config.py

PRODUCT_COUNT = 500
CUSTOMER_COUNT = 5000
STORE_COUNT = 20

EVENTS_PER_MINUTE = 200

# Realistic behavior weights
EVENT_WEIGHTS = {
    "product_view": 0.70,
    "add_to_cart": 0.20,
    "order": 0.08,
    "return": 0.02
}

# Time behavior (peak hours)
HOUR_WEIGHTS = {
    0: 0.1, 1: 0.05, 2: 0.05, 3: 0.05,
    8: 0.5, 9: 0.8, 10: 1.0, 11: 1.2,
    12: 1.5, 13: 1.3, 14: 1.2, 15: 1.1,
    16: 1.3, 17: 1.5, 18: 2.0, 19: 2.2,
    20: 2.0, 21: 1.5, 22: 1.0, 23: 0.5
}