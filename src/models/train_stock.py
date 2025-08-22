import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from ..data.make_dataset import create_synthetic_stock


def featurize(df, lags=5):
    X = []
    y = []
    for i in range(lags, len(df)):
        X.append(df['close'].values[i-lags:i])
        y.append(df['close'].values[i])
    return np.array(X), np.array(y)


def train_and_save(output_path='model_artifacts/stock_model.pkl'):
    df = create_synthetic_stock()
    X, y = featurize(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    print('MSE:', mse)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    joblib.dump(model, output_path)
    return model


if __name__ == '__main__':
    train_and_save()
