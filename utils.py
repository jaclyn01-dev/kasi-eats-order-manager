"""Helper functions for Kasi Eats Order Manager."""

import json
import csv
from datetime import datetime
from models import MenuItem

def apply_discount(subtotal):
    """Return the discount amount: 10% of subtotal if subtotal is R200 or more, else 0."""
    if subtotal >= 200:
        return subtotal * 0.10
    return 0.0

def load_menu(filepath):
    """Load the menu from JSON and return a dict of name -> MenuItem."""
    with open(filepath) as f:
        raw = json.load(f)
    return {name: MenuItem(name, price) for name, price in raw.items()}

def save_sale(order, total):
    """Append one order to data/sales.csv."""
    with open("data/sales.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            json.dumps(order),
            f"{total:.2f}"
        ])

def load_sales():
    """Read data/sales.csv and return a list of sale dicts."""
    try:
        f = open("data/sales.csv")
    except FileNotFoundError:
        return []
    sales = []
    with f:
        reader = csv.DictReader(f)
        for row in reader:
            sales.append({
                "datetime": row["datetime"],
                "items": json.loads(row["items"]),
                "total": float(row["total"])
            })
    return sales

def daily_summary():
    """Print number of orders, total takings, and best-selling item."""
    sales = load_sales()

    if not sales:
        print("No sales yet today.")
        return

    total_takings = 0
    item_counts = {}
    for sale in sales:
        total_takings += sale["total"]
        for name, qty, line_total in sale["items"]:
            item_counts[name] = item_counts.get(name, 0) + qty

    best_seller = max(item_counts, key=item_counts.get)

    print(f"Orders today: {len(sales)} | Takings: R {total_takings:.2f} | Best seller: {best_seller.title()}")