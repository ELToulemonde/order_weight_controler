import os
from os.path import join

DATA_PATH = os.path.dirname(__file__)
ORDERS_FILE = join(DATA_PATH, "orders.json")
CONTROL_PATH = join(DATA_PATH, "control.parquet")
