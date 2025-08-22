from flask import Blueprint, request, jsonify
import os
import pickle
import logging

api_bp = Blueprint("api", __name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_DIR = os.path.join(BASE_DIR, "model_artifacts")
MODEL_PATH = os.path.join(MODEL_DIR, "stock_model.pkl")

logger = logging.getLogger(__name__)


def _load_model(path):
    # Try joblib first (faster for sklearn objects), fallback to pickle
    try:
        import joblib

        return joblib.load(path)
    except Exception as e:
        logger.debug("joblib load failed: %s", e)
        with open(path, "rb") as f:
            return pickle.load(f)


@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@api_bp.route("/predict_price", methods=["POST"])
def predict_price():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "invalid or missing json body"}), 400

    features = data.get("features")
    if not isinstance(features, (list, tuple)):
        return jsonify({"error": "features must be a list of numbers"}), 400

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
        # fallback naive prediction
        try:
            return jsonify({"prediction": sum(features) / len(features)})
        except Exception:
            return jsonify({"error": "prediction failed"}), 500


@api_bp.route("/segment", methods=["POST"])
def segment():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "invalid or missing json body"}), 400

    X = data.get("data")
    if not isinstance(X, (list, tuple)):
        return jsonify({"error": "data must be a list of feature rows"}), 400

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
