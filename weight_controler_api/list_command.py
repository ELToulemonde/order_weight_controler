import json

from data import ORDERS_FILE


def list_command():
    with open(ORDERS_FILE, 'r') as f:
        data = json.load(f)
    return [elt["order_id"] for elt in data]
