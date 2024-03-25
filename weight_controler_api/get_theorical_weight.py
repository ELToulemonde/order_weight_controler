from os.path import join

import pandas as pd

from balance.get_weight import load_order
from data import DATA_PATH


def get_theorical_weight(order_id):
    order = load_order(order_id)
    weights = pd.read_csv(join(DATA_PATH, "products_weights.csv"))
    total_weight = 0
    for order_element in order["content"]:
        total_weight += order_element["quantity"] * weights.loc[order_element["product_id"], "theoretical_weight"]
    return total_weight
