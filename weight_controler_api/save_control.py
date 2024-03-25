import sqlite3

import pandas as pd


def save_control(order_id, test_weight, weight_theorical, weight_real, employee_id):
    df = pd.DataFrame({"order_id": [order_id], "theoretical_weight": [weight_theorical], "weight_real": [weight_real],
                       "test_weight": [test_weight],"employee_id": [employee_id]})
    conn = sqlite3.connect('weight_controller.db')
    df.to_sql("hist_control", conn, if_exists="append")
