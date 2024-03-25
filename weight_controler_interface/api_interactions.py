import requests


def get_command_list():
    response = requests.get("http://0.0.0.0:8000/command/list")
    if response.status_code == 200:
        return response.json()
    else:
        return []


def send_control_command(command_id, employee_id):
    response = requests.get(f"http://0.0.0.0:8000/control?order_id={command_id}&employee_id={employee_id}")
    if response.status_code == 200:
        return response.json()["status"]
    else:
        return "error"


def get_employee_list():
    return requests.get("http://0.0.0.0:8000/employee/list").json()



# Fonction pour obtenir la liste des produits depuis l'API
def get_product_list():
    response = requests.get("http://0.0.0.0:8000/product/list")
    if response.status_code == 200:
        return response.json()
    else:
        return []
