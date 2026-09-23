import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("books_dataset.csv")

print()
print("==========================================")
print("        BOOK DATASET ANALYSIS")
print("==========================================")

print()
print("First 10 books:")
print(df.head(10))


# ==========================================
# BASIC INFORMATION
# ==========================================

print()
print("===== BASIC STATISTICS =====")

total_books = len(df)
average_price = df["Price"].mean()
highest_price = df["Price"].max()
lowest_price = df["Price"].min()

print(f"Total number of books: {total_books}")
print(f"Average price: £ {average_price:.2f}")
print(f"Highest price: £ {highest_price:.2f}")
print(f"Lowest price: £ {lowest_price:.2f}")


# ==========================================
# MOST EXPENSIVE BOOK
# ==========================================

most_expensive = df.loc[df["Price"].idxmax()]

print()
print("===== MOST EXPENSIVE BOOK =====")
print(f"Title: {most_expensive['Title']}")
print(f"Price: £ {most_expensive['Price']:.2f}")


# ==========================================
# CHEAPEST BOOK
# ==========================================

cheapest = df.loc[df["Price"].idxmin()]

print()
print("===== CHEAPEST BOOK =====")
print(f"Title: {cheapest['Title']}")
print(f"Price: £ {cheapest['Price']:.2f}")


# ==========================================
# AVAILABILITY
# ==========================================

print()
print("===== AVAILABILITY =====")

availability_count = df["Availability"].value_counts()

print(availability_count)


# ==========================================
# TOP 10 MOST EXPENSIVE BOOKS
# ==========================================

top_10 = df.nlargest(10, "Price").sort_values("Price")

plt.figure(figsize=(12, 7))

plt.barh(
    top_10["Title"],
    top_10["Price"]
)

plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.title("Top 10 Most Expensive Books")

plt.tight_layout()
plt.show()


# ==========================================
# TOP 10 CHEAPEST BOOKS
# ==========================================

bottom_10 = df.nsmallest(10, "Price").sort_values("Price")

plt.figure(figsize=(12, 7))

plt.barh(
    bottom_10["Title"],
    bottom_10["Price"]
)

plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.title("Top 10 Cheapest Books")

plt.tight_layout()
plt.show()


# ==========================================
# PRICE DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["Price"],
    bins=15,
    edgecolor="black"
)

plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.title("Book Price Distribution")

plt.tight_layout()
plt.show()


# ==========================================
# AVAILABILITY CHART
# ==========================================

plt.figure(figsize=(8, 5))

availability_count.plot(
    kind="bar"
)

plt.xlabel("Availability")
plt.ylabel("Number of Books")
plt.title("Book Availability")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ==========================================
# FINAL MESSAGE
# ==========================================

print()
print("==========================================")
print("          ANALYSIS COMPLETED")
print("==========================================")