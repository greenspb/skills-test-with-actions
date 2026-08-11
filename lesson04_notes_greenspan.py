python -m venv .venv/calculations
source .venv/calculations/bin/activate
pip install -r requirements.txt
pip install pytest coverage pytest-cov

pytest --cov=src --verbose

