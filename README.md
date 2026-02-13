# MathBooks

A Python script that fetches mathematics books from the Open Library API and exports them to a CSV file.

## Description

MathBooks queries the [Open Library API](https://openlibrary.org) to retrieve books categorized under the "math" subject and filters them to include only books published after the year 2000. The results are saved in a CSV file format for easy analysis and reference.

## Features

- Fetches up to 50 mathematics books from Open Library
- Filters books published after 2000
- Exports data to CSV format including:
  - Book title
  - Author name
  - First publication year
  - Publisher
- Handles API errors gracefully

## Requirements

- Python 3.6 or higher
- requests library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mnnjbb2006-cmyk/MathBooks.git
cd MathBooks
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python main.py
```

The script will create a `books.csv` file in the current directory containing the mathematics books data.

## Output Format

The generated CSV file includes the following columns:
- **Title**: The title of the book
- **Author**: The primary author's name
- **Year**: The first publication year
- **Publisher**: The primary publisher's name

## Example Output

```csv
Title,Author,Year,Publisher
Advanced Calculus,John Smith,2015,Academic Press
Linear Algebra and Its Applications,Jane Doe,2010,Wiley
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Mani Jabbari (mnnjbb.2006@gmail.com)

## Acknowledgments

- Data provided by [Open Library](https://openlibrary.org)
