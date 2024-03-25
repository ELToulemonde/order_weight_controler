from balance.get_weight import get_weight
from weight_controler_api.get_theorical_weight import get_theorical_weight
from weight_controler_api.save_control import save_control


def control(order_id, employee_id):
    weight_theorical = get_theorical_weight(order_id=order_id)
    weight_real = get_weight(order_id=order_id)
    test_weight = abs(weight_theorical - weight_real) / weight_theorical < 0.05
    save_control(order_id=order_id, test_weight=test_weight, weight_theorical=weight_theorical, weight_real=weight_real,
                 employee_id=employee_id)
    return test_weight
