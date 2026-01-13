import pandas as pd

def load_demand_data(path: str):
    df = pd.read_csv(path, parse_dates=["date"])
    df = df.sort_values("date")
    return df
