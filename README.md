# Hacker News Scraper

Simple Python project that scrapes headlines from Hacker News and saves them into a dated text file.

## Features

- Connects to Hacker News
- Extracts current headlines
- Saves results into a `.txt` file
- Generates the output file automatically with the current date

## How to run

1. Activate the virtual environment
2. Run the script:

python main.py

## Output

The program generates a file like:

hn_headlines_2026-03-26.txt

The file contains:

- Project title
- Date
- Source URL
- Numbered list of headlines

## Tech used

- Python
- requests
- BeautifulSoup

## Notes

- If the request fails, the program stops and shows an error message
- The scraper currently works with the Hacker News homepage