from src.models.train_stock import featurize
import pandas as pd


def test_featurize():
    df = pd.DataFrame({"close": [1, 2, 3, 4, 5, 6, 7]})
    X, y = featurize(df, lags=3)
    assert X.shape[0] == 4
    assert X.shape[1] == 3
