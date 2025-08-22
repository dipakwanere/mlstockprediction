import os
from ..data.make_dataset import create_synthetic_stock


def featurize(df, lags=5):
    """Lightweight featurize that operates on pandas Series without importing numpy at module import time."""
    X = []
    y = []
    # Support pandas DataFrame or plain dict/list for 'close'
    closes_obj = (
        df["close"] if isinstance(df, dict) or hasattr(df, "__getitem__") else None
    )
    if closes_obj is None:
        # attempt attribute access
        closes_obj = getattr(df, "close", None)

    # extracts values: if object has .values use it, else assume it's list-like
    if hasattr(closes_obj, "values"):
        closes = list(closes_obj.values)
    else:
        closes = list(closes_obj)
    for i in range(lags, len(closes)):
        X.append(closes[i - lags : i])
        y.append(closes[i])
    return X, y


def train_and_save(output_path="model_artifacts/stock_model.pkl"):
    # Import heavy libs lazily to avoid import-time failures
    import joblib
    import numpy as np
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error

    df = create_synthetic_stock()
    X, y = featurize(df)
    X = np.array(X)
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    print("MSE:", mse)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    joblib.dump(model, output_path)
    return model


if __name__ == "__main__":
    train_and_save()
