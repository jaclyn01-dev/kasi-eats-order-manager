# Kasi Eats Order Manager

A command-line order management system for Mama Thandi's Soweto food stall. It lets a cashier take orders from a menu, calculate totals with VAT and discounts, handle cash and change, and view a daily sales summary.

## How to Run

Make sure you have Python 3 installed, then clone the repo and run:

```bash
git clone https://github.com/jaclyn01-dev/kasi-eats-order-manager.git
cd kasi-eats-order-manager
python main.py
```

## Features

- Welcome banner with stall name and location
- Cashier login greeting
- Menu loaded from `data/menu.json`
- Take an order with multiple items and quantities
- 10% discount applied automatically when subtotal is R200 or more
- VAT (15%) calculated on the discounted amount
- Itemised receipt with aligned columns
- Cash and change calculation with R10 coin breakdown
- Daily sales summary: number of orders, total takings, and best-selling item
- Sales saved to `data/sales.csv` after each order
- Input validation on quantity and cash paid

## Concepts Used

- Variables and data types (str, float, int, bool)
- Constants (`MENU`, `VAT_RATE`)
- f-strings and string formatting (`.upper()`, `.center()`, `:<15`, `:>6.2f`)
- `while True` loops with `break` and `continue`
- `if / elif / else` conditionals
- Functions with docstrings
- Dictionaries, lists, sets, and tuples
- Classes and objects (`MenuItem`, `Order`)
- File I/O: JSON (read) and CSV (read/write)
- Exception handling (`try / except ValueError`, `FileNotFoundError`)
- `enumerate()`, `f-string` alignment, `//` and `%` operators
- Modules: splitting code across `main.py`, `models.py`, `utils.py`

## Sample Run

```
==================================================
      KASI EATS ORDER MANAGER - SOWETO
==================================================
Cashier name: Thabo
Sawubona, Thabo! Let's sell some kotas.
MAIN MENU
1. New Order
2. View Menu
3. Daily Summary
4. Exit
Choose an option: 1
Item (or 'done'): kota
Quantity: 2
Item (or 'done'): cooldrink
Quantity: 1
Item (or 'done'): done
RECEIPT
Kota              2      R  70.00
Cooldrink         1      R  15.00
Subtotal                 R  85.00
VAT (15%)                R  12.75
TOTAL                    R  97.75
Cash paid: 100
Change                   R   2.25
(0 x R10 + R 2.25)
```

## Help Received

Used an AI assistant for tutoring and code review on structure, class design, and debugging (unsaved-file errors, indentation, `calculate_total` return shape). All code was typed by me and tested at each milestone.

## Author

- **Name:** Jaclyn Moses
- **Cohort:** Empodera Software Development NQF Level 5
- **Date:** 3 November 2026
