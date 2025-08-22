import os
import joblib
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def train_and_save(output_path="model_artifacts/seg_model.pkl"):
    X, _ = make_blobs(n_samples=500, centers=4, n_features=4, random_state=42)
    km = KMeans(n_clusters=4, random_state=42)
    km.fit(X)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    joblib.dump(km, output_path)
    return km


if __name__ == "__main__":
    train_and_save()
