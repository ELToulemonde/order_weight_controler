import json

from fastapi import FastAPI

from caisse import new_order
from data import ORDERS_FILE
from logger import logger
from weight_controler_api.command_status import CommandStatus
from weight_controler_api.control_order import control_order

app = FastAPI()


@app.get("/health")
def health():
    return {"message": "OK"}


@app.get("/control")
def control_api(command_id: str):
    logger.info(" i am controlling command {}".format(command_id))
    result = control_order(command_id)
    logger.info("i am finished controlling command {}".format(command_id))
    if not result:
        return {"message": CommandStatus.not_ok}
    return {"message": CommandStatus.ok}


def list_commands():
    with open(ORDERS_FILE, 'r') as f:
        data = json.load(f)
    list_commands = [elt['order_id'] for elt in data]
    return list_commands

@app.post("/new_command")
def new_command_api():
    return new_order()

@app.get("/list_command")
def list_commands_api():
    return list_commands()
