rm -rf .venv dist
poetry install
poetry build
pip install twine
twine upload  --verbose -r testpypi dist/*
rm -rf .venv dist