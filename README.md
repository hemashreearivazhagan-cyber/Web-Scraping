# Web-Scraping
A Python-based web scraping project that extracts 1,000 book records from 50 web pages, stores them in a CSV dataset, and performs data analysis and visualization using Pandas and Matplotlib.
# 📚 Web Scraping and Book Data Analysis

## 📌 Project Overview

This project is a Python-based **Web Scraping and Data Analysis** project.

The project collects book information from the **Books to Scrape** website and extracts details such as:

- 📖 Book Title
- 💷 Price
- 📦 Availability

The website contains multiple pages, so the project uses **pagination** to scrape data from all 50 pages.

A total of **1,000 book records** are collected and stored in a CSV file. The collected dataset is then analyzed using Python libraries such as **Pandas** and visualized using **Matplotlib**.

---

## 🎯 Objectives

- Learn how web scraping works using Python.
- Extract structured information from a website.
- Scrape data from multiple pages.
- Store scraped data in a CSV dataset.
- Perform basic data analysis.
- Generate visualizations from the collected data.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | Connect to the website |
| BeautifulSoup | Extract data from HTML |
| Pandas | Data processing and analysis |
| Matplotlib | Data visualization |
| CSV | Store the scraped dataset |

---

## 📂 Project Structure

```text
Web Scraping/
│
├── web_scraping.py
├── analysis.py
├── books_dataset.csv
└── README.md
