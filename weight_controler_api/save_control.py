import pandas as pd

from data import CONTROL_PATH


def save_control(command_id, real_weight, theorical_weight, result):
    old_df = pd.read_parquet(CONTROL_PATH)
    df = pd.DataFrame({"order_id": [command_id], "real_weight": [real_weight], "theorical_weight": [theorical_weight],
                       "result": [result]})
    df = pd.concat([old_df, df])
    df.to_parquet(CONTROL_PATH, index=False)
