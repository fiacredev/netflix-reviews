.PHONY: help setup check notebook sentiment topics clean

help:
	@echo "Netflix reviews analysis"
	@echo ""
	@echo "  make setup      Install the Python dependencies"
	@echo "  make check      Summarise the raw dataset"
	@echo "  make notebook   Start JupyterLab with the analysis notebook"
	@echo "  make sentiment  Print the sentiment distribution"
	@echo "  make topics     Train the LDA topic model"
	@echo "  make clean      Remove generated artifacts and caches"

setup:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

check:
	python scripts/inspect_dataset.py

notebook:
	jupyter lab netflix.ipynb

sentiment:
	python scripts/sentiment_summary.py

topics:
	python scripts/topic_modeling.py

clean:
	rm -rf outputs .ipynb_checkpoints .pytest_cache
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
