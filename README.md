# Math books — OpenLibrary CSV exporter

A small utility that queries the OpenLibrary Search API for math-related books and writes a filtered CSV (`books.csv`). `main.py` is a single-script entrypoint that performs the API call and writes the CSV.

## Features
- Queries `https://openlibrary.org/search.json` with a `User-agent` header.
- Filters results to include only entries where `first_publish_year` exists and is > 2000.
- Writes `books.csv` with the stable header ordering: `Title, Author, Year, Publisher`.

## Repository structure
- `main.py` — script entrypoint that calls the OpenLibrary API and writes `books.csv`.
- `books.csv` — generated output (created by running `main.py`).
- `requirements.txt` — Python dependencies used by the project.
- `LICENSE` — project license.

## Recommended setup (create an isolated virtual environment)
Use a virtual environment (venv) to keep dependencies isolated. The examples below use `python3` — adjust if your system uses a different executable.

```zsh
# Create and activate a venv in the project directory
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If you prefer `virtualenv` or `conda`, use your usual workflow instead.

## Run the script
After activating your virtual environment and installing dependencies, run:

```zsh
python main.py
```

This will produce or update `books.csv` in the repository root.

## Behavior and API notes
- Network call: `main.py` uses the OpenLibrary Search API `https://openlibrary.org/search.json`. The script sets a `User-agent` header. If you modify the request, keep a polite `User-agent`.

## Development tips
- Keep API calls small while iterating to avoid API rate limits. When developing, set any request `limit` parameter to a small number or mock `requests.get` in tests.

## Troubleshooting
- If you see network errors, check connectivity and OpenLibrary availability. Retry with a smaller `limit` or run later.
- If `requirements.txt` is missing or incomplete, add `requests` (and any other runtime deps) and re-run `pip install -r requirements.txt`.

## Contributing
- Update `requirements.txt` if you add new dependencies.

## License
See the `LICENSE` file in the repository for license details.

---
