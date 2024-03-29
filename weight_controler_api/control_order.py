from balance.get_weight import get_weight
from logger import logger
from weight_controler_api.get_theorical_weight import get_theorical_weight
from weight_controler_api.save_control import save_control


def control_order(command_id):
    real_weight = get_weight(order_id=command_id)
    theorical_weight = get_theorical_weight(order_id=command_id)
    result = abs(real_weight - theorical_weight) / theorical_weight < 0.05
    save_control(command_id, real_weight, theorical_weight, result)
    logger.info(
        f"for command{command_id} the real weight is {real_weight}, the theorical weight is {theorical_weight}, "
        f"the result is {result}")
    return result
