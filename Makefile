install:
	python -m venv .venv; .venv\Scripts\pip install -r requirements.txt

run:
	python -m app.main

train:
	python -m src.models.train_stock
