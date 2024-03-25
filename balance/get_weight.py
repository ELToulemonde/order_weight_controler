import json
import random
from posixpath import join

import pandas as pd

from data import ORDERS_FILE, DATA_PATH

ERROR_RATE = 0.2


def load_order(order_id):
    with open(ORDERS_FILE, 'r') as f:
        data = json.load(f)
    for order in data:
        if order["order_id"] == order_id:
            return order


def drop_random_item(order):
    content = order["content"]
    content.pop(random.randint(0, len(content) - 1))
    order["content"] = content
    return order


def manual_process(order):
    if random.random() < ERROR_RATE:
        order = drop_random_item(order)
    return order


def load_theoretical_weights() -> pd.DataFrame:
    return pd.read_csv(join(DATA_PATH, 'products_weights.csv'))


def get_weight(order_id):
    order = load_order(order_id)
    order = manual_process(order)
    weights = load_theoretical_weights()
    real_weight = []
    if len(order["content"]) == 0:
        return 0
    for elt in order['content']:
        weight_unit = (weights.loc[elt["product_id"], "theoretical_weight"] + random.randint(-1, 1) * weights.loc[
            elt["product_id"], "std"])
        real_weight.append(weight_unit * elt["quantity"])
    return sum(real_weight)


if __name__ == '__main__':
    print(get_weight("82d7838a-7d45-4ad1-8981-88e35514fcc3"))
