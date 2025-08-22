import pandas as pd
import numpy as np


def create_synthetic_stock(n=500, seed=42):
    np.random.seed(seed)
    t = np.arange(n)
    prices = 100 + np.cumsum(np.random.normal(0, 1, size=n)) + 0.1 * t
    dates = pd.date_range("2020-01-01", periods=n)
    df = pd.DataFrame({"date": dates, "close": prices})
    return df
