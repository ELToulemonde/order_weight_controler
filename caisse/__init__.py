import json
import random
import uuid
from posixpath import join

import pandas as pd

from data import DATA_PATH, ORDERS_FILE


def new_order() -> dict:
    products = pd.read_csv(join(DATA_PATH, 'products_weights.csv'), usecols=['product_id', 'product_name'])
    number_of_products = random.randint(1, 5)
    selected_products = random.choices(products["product_id"].tolist(), k=number_of_products)
    selected_quantities = random.choices(range(0, 5), k=number_of_products)
    order = products.loc[selected_products]
    order["quantity"] = selected_quantities
    order_dict = {
        "order_id": uuid.uuid4().__str__(),
        "content": [
            order.iloc[row].to_dict() for row in range(len(order))
        ]
    }
    save_order(order_dict)
    return order_dict


def save_order(order_dict):
    with open(ORDERS_FILE, 'r') as f:
        orders = json.load(f)
    with open(ORDERS_FILE, 'w') as f:
        orders.append(order_dict)
        json.dump(orders, f)


if __name__ == '__main__':
    print(new_order())
