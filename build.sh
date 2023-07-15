rm -rf .venv dist
poetry install
poetry build
pip install twine
twine upload  --verbose dist/*
rm -rf .venv dist