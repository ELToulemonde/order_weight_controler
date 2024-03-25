from os.path import join

import pandas as pd
from fastapi import FastAPI

from data import DATA_PATH
from logger import logger
from weight_controler_api.control import control
from weight_controler_api.list_command import list_command
from weight_controler_api.list_employee import list_employee

app = FastAPI()


@app.get("/health")
def health_api():
    return {"status": "ok"}


@app.get("/control")
def control_api(order_id: str, employee_id: int):
    logger.info(f"start controling order_id: {order_id}")
    test_weight = control(order_id, employee_id)
    logger.info(f"end controling order_id: {order_id}")
    if test_weight:
        return {"status": "OK !"}
    else:
        return {"status": "NOT OK !"}


@app.get("/command/list")
def list_command_api():
    return list_command()


@app.get("/employee/list")
def employee_list_api():
    return list_employee()


def list_product():
    return pd.read_csv(join(DATA_PATH, "products_weights.csv"))["product_name"].to_list()


@app.get("/product/list")
def product_list_api():
    return list_product()
