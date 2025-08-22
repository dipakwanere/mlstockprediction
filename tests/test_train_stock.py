from src.models.train_stock import featurize


def test_featurize():
    # use a plain dict to avoid importing pandas/numpy during test collection
    df = {"close": [1, 2, 3, 4, 5, 6, 7]}
    X, y = featurize(df, lags=3)
    assert isinstance(X, list)
    assert isinstance(y, list)
    assert len(X) == 4
    assert len(X[0]) == 3
