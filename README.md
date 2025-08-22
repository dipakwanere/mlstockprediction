# ML-Ops Stock Prediction & Segmentation Template

This repository is a starter ML-Ops project for stock price prediction and customer segmentation. It includes:

- Flask API for serving models
- Training pipelines for time-series forecasting (stock price prediction) and clustering (segmentation)
- Example notebooks and unit tests
- Dockerfile and docker-compose for local dev
- GitHub Actions CI/CD workflows for tests and Docker build

See the `docs/` folder for more details and the `scripts/` for quick commands.

Quick start
1. Create a Python virtual environment and install dependencies from `requirements.txt`.
2. Run `python -m app.main` to start the Flask API (or use docker-compose).
