import requests


def predict_sample():
    payload = {"features": [100, 101, 102, 103, 104]}
    r = requests.post("http://localhost:5000/predict_price", json=payload)
    print("response", r.json())


if __name__ == "__main__":
    predict_sample()
