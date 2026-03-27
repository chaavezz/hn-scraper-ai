Hacker News Scraper

Simple Python project that scrapes headlines from Hacker News and saves them into both a structured JSON file and a readable TXT report.

Features
	•	Connects to Hacker News
	•	Extracts current headlines and their URLs
	•	Stores data in structured format (JSON)
	•	Generates a clean and readable TXT report
	•	Automatically names output files with the current date

How to run
	1.	Activate the virtual environment
	2.	Run the script:

python main.py

Output

The program generates two files:

hn_headlines_YYYY-MM-DD.txt
hn_headlines_YYYY-MM-DD.json

TXT file

Human-readable report containing:
	•	Project title
	•	Date
	•	Source URL
	•	Numbered list of headlines with links

JSON file

Structured data format containing:
	•	Title of each headline
	•	URL of each headline

Tech used
	•	Python
	•	requests
	•	BeautifulSoup
	•	json

Notes
	•	If the request fails, the program stops and shows an error message
	•	The scraper is currently designed for the Hacker News homepage
	•	JSON output can be used for further processing, automation, or integration with AI tools

Purpose

This project demonstrates:
	•	Web scraping
	•	HTML parsing
	•	Data structuring
	•	File generation (TXT + JSON)
	•	Basic error handling in Python