import os
import pickle

os.makedirs("model_artifacts", exist_ok=True)


# Dummy stock model: object with predict method
class DummyStockModel:
    def predict(self, X):
        # X is list-like, return average of each row
        out = []
        for row in X:
            try:
                out.append(sum(row) / len(row))
            except Exception:
                out.append(0.0)
        return out


class DummySegModel:
    def predict(self, X):
        return [0 for _ in X]


with open("model_artifacts/stock_model.pkl", "wb") as f:
    pickle.dump(DummyStockModel(), f)

with open("model_artifacts/seg_model.pkl", "wb") as f:
    pickle.dump(DummySegModel(), f)

print("Dummy artifacts written to model_artifacts/")
