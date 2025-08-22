from flask import Blueprint, request, jsonify
import joblib
import os

api_bp = Blueprint('api', __name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model_artifacts', 'stock_model.pkl')


@api_bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@api_bp.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.json
    # Expect feature list or last N prices; here we'll accept a simple numeric feature vector
    features = data.get('features')
    if features is None:
        return jsonify({'error': 'missing features'}), 400

    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        pred = model.predict([features])
        return jsonify({'prediction': float(pred[0])})
    else:
        # fallback mock prediction
        return jsonify({'prediction': sum(features) / len(features)})


@api_bp.route('/segment', methods=['POST'])
def segment():
    data = request.json
    X = data.get('data')
    if X is None:
        return jsonify({'error': 'missing data'}), 400

    # Use a simple KMeans saved model
    CLUSTER_PATH = os.path.join(os.path.dirname(__file__), '..', 'model_artifacts', 'seg_model.pkl')
    if os.path.exists(CLUSTER_PATH):
        km = joblib.load(CLUSTER_PATH)
        labels = km.predict(X)
        return jsonify({'labels': labels.tolist()})
    else:
        # naive segmentation: assign 0 to all
        return jsonify({'labels': [0 for _ in X]})
