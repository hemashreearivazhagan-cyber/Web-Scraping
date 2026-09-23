import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

books = []

print("Starting web scraping...\n")

# Scrape all 50 pages
for page in range(1, 51):

    url = BASE_URL.format(page)

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Page {page} failed!")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    book_items = soup.select("article.product_pod")

    for book in book_items:

        # Book title
        title = book.h3.a["title"]

        # Price
        price_text = book.select_one(".price_color").text.strip()

        # Convert price to number
        price = float(
            price_text.replace("£", "").replace("Â", "")
        )

        # Availability
        availability = book.select_one(".availability").get_text(strip=True)

        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

    print(
        f"Page {page}/50 scraped successfully - "
        f"{len(book_items)} books"
    )

# Create DataFrame
df = pd.DataFrame(books)

print("\n===================================")
print("WEB SCRAPING COMPLETED!")
print("===================================")

print(f"Total books scraped: {len(df)}")

print("\nFirst 10 books:")
print(df.head(10))

# Save dataset
df.to_csv(
    "books_dataset.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nDataset saved successfully!")
print("File: books_dataset.csv")