from os.path import join

import pandas as pd

from balance.get_weight import load_order
from data import DATA_PATH


def get_theorical_weight(order_id):
    order = load_order(order_id=order_id)
    weight_df = pd.read_csv(join(DATA_PATH, "products_weights.csv"))
    total_weight = 0
    for product in order["content"]:
        total_weight += weight_df.loc[product["product_id"], "theoretical_weight"] * product["quantity"]
    return total_weight
