# ML-Ops Stock Prediction & Segmentation Template

This repository is a production-ready MLOps project that implements stock price prediction and customer segmentation models with a focus on maintainability, scalability, and best practices.

## Project Overview

### Features
- **Stock Price Prediction**: Time series forecasting model for predicting stock prices
- **Customer Segmentation**: ML model for segmenting customers based on their trading patterns
- **RESTful API**: Flask-based API for real-time predictions and segmentation
- **Containerization**: Docker setup for consistent development and deployment
- **CI/CD Pipeline**: Automated testing and deployment using GitHub Actions
- **Model Versioning**: Tracking model artifacts and metadata

### Technology Stack
- **Framework**: Flask + Flask-RESTful
- **ML Libraries**: scikit-learn, pandas, numpy
- **Visualization**: matplotlib
- **Deployment**: Docker, Gunicorn
- **Testing**: pytest
- **CI/CD**: GitHub Actions

### Directory Structure
- `app/`: Flask application and API endpoints
- `src/`: 
  - `models/`: Training pipelines for stock and segmentation models
  - `data/`: Data processing and dataset creation
- `model_artifacts/`: Trained models and their metadata
- `tests/`: Unit and integration tests
- `docs/`: Project documentation and architecture details
- `scripts/`: Utility scripts for development and deployment

See `docs/ARCHITECTURE.md` for architecture details.

Quick start
1. Create and activate a Python virtual environment, then install dependencies:

```powershell
python -m venv .venv
.venv\Scripts\pip install --upgrade pip
.venv\Scripts\pip install -r requirements.txt
```

2. Run the API locally:

```powershell
python -m app.main
```

3. Train models (writes to `model_artifacts/`):

```powershell
python -m src.models.train_stock
python -m src.models.train_segment
```

## API Endpoints

### Stock Prediction
- `POST /predict/stock`
  - Input: JSON with stock symbol and historical data
  - Output: Predicted price movements

### Customer Segmentation
- `POST /segment/customer`
  - Input: JSON with customer trading history
  - Output: Segment classification and characteristics

## Development Setup

### Prerequisites
- Python 3.11+
- Docker and docker-compose
- Git

### Local Development
1. Clone the repository:
```bash
git clone https://github.com/dipakwanere/mlstockprediction.git
cd mlstockprediction
```

2. Create and activate a Python virtual environment, then install dependencies:
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. Run the API locally:
```powershell
python -m app.main
```

4. Train models (outputs to `model_artifacts/`):
```powershell
python -m src.models.train_stock
python -m src.models.train_segment
```

### Docker Setup
1. Build and run using docker-compose:
```bash
docker-compose up --build
```

2. Access the API at `http://localhost:5000`

## Testing
Run the test suite:
```bash
pytest tests/
```

## Notes
- If you see binary import errors for numpy/scikit-learn on Windows, use conda to create an environment with prebuilt binaries (recommended)
- See `docs/ARCHITECTURE.md` for detailed system design and architecture
- Models are versioned and stored in `model_artifacts/` with accompanying metadata
- CI/CD pipeline runs tests and builds Docker images for each PR

## Contributing
Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


