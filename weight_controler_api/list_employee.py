from os.path import join

import pandas as pd

from data import DATA_PATH


def list_employee():
    df = pd.read_csv(join(DATA_PATH, "employee.csv"))
    return df["id"].to_list()
