# PWC- Price Comparision Website

A simple yet effective web application that allows users to compare mobile phone prices between Amazon and Flipkart based on specific search criteria such as product name, storage, RAM, and price range.

## Features

- Search by product name, storage, RAM, and price range
- Compare product prices from Flipkart and Amazon
- Direct links to product listings on both platforms
- Intelligent matching of product names, color, storage, and RAM
- User-friendly UI with responsive styling

### Comparison Results

- Flipkart and Amazon product details displayed side-by-side
- Easy-to-read format and direct links to buy

## Tech Stack

| Layer         | Technology         |
|---------------|--------------------|
| Frontend      | HTML, CSS          |
| Backend       | Flask (Python)     |
| Scraping      | BeautifulSoup, Requests |
| Data Storage  | CSV files          |

## Project Structure

```
.
├── app.py                # Flask backend application
├── webscraping.py        # Web scraping logic for Amazon & Flipkart
├── templates/
│   ├── index.html        # Homepage with product form
│   └── display.html      # Results display page
├── static/
│   └── style.css         # Custom CSS styling
├── amazon.csv            # Scraped Amazon product data
├── flipkart.csv          # Scraped Flipkart product data
└── test.html             # Temporary HTML file for Amazon scraping
```
## Prerequisites

Make sure you have the following installed:

- Python
- pip (Python package installer)
- flask
- BeautifulSoup
- Pandas


## Run
Run the Flask app- python app.py


## How It Works

1. User fills out the product form with specifications.
2. On form submission, Flask triggers the `/compare` route.
3. The backend:
   - Scrapes Flipkart and Amazon with the given search term.
   - Saves data in `amazon.csv` and `flipkart.csv`.
   - Filters matching entries based on RAM and price.
   - Renders `display.html` with matching results.

## Disclaimer

- Amazon might block frequent requests. Use responsibly.
- Flipkart and Amazon may update their HTML structure, which may break scraping logic.

