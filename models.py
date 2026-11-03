"""Data models for Kasi Eats Order Manager."""


class MenuItem:
    """A single item on the menu."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name.title():<15} R {self.price:>6.2f}"

class Order:
    """A customer order: a list of (item_name, qty, line_total) tuples."""

    def __init__(self):
        self.items = []

    def add_item(self, name, qty, line_total):
        """Add one line to the order."""
        self.items.append((name, qty, line_total))

    def subtotal(self):
        """Return the sum of all line totals."""
        return sum(line_total for name, qty, line_total in self.items)

    def total(self, vat_rate):
        """Return the grand total after discount and VAT."""
        subtotal = self.subtotal()
        discount = subtotal * 0.10 if subtotal >= 200 else 0.0
        taxable = subtotal - discount
        return taxable + taxable * vat_rate