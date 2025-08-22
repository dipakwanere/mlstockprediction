from flask import Blueprint, request, jsonify
import os
import pickle

api_bp = Blueprint("api", __name__)

MODEL_PATH = os.path.join(
    os.path.dirname(__file__), "..", "model_artifacts", "stock_model.pkl"
)


def _load_model(path):
    # Try joblib first (faster for sklearn objects), fallback to pickle
    try:
        import joblib

        return joblib.load(path)
    except Exception:
        with open(path, "rb") as f:
            return pickle.load(f)


@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@api_bp.route("/predict_price", methods=["POST"])
def predict_price():
    data = request.json
    features = data.get("features")
    if features is None:
        return jsonify({"error": "missing features"}), 400

    if os.path.exists(MODEL_PATH):
        model = _load_model(MODEL_PATH)
        try:
            pred = model.predict([features])
            return jsonify({"prediction": float(pred[0])})
        except Exception:
            # If model is a simple callable object
            try:
                return jsonify({"prediction": float(model.predict(features))})
            except Exception:
                return jsonify({"error": "model prediction failed"}), 500
    else:
        return jsonify({"prediction": sum(features) / len(features)})


@api_bp.route("/segment", methods=["POST"])
def segment():
    data = request.json
    X = data.get("data")
    if X is None:
        return jsonify({"error": "missing data"}), 400

    CLUSTER_PATH = os.path.join(
        os.path.dirname(__file__), "..", "model_artifacts", "seg_model.pkl"
    )
    if os.path.exists(CLUSTER_PATH):
        km = _load_model(CLUSTER_PATH)
        try:
            labels = km.predict(X)
            # ensure list
            return jsonify({"labels": list(map(int, labels))})
        except Exception:
            # fallback: naive labels
            return jsonify({"labels": [0 for _ in X]})
    else:
        return jsonify({"labels": [0 for _ in X]})
