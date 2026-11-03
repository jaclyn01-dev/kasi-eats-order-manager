from models import Order
from utils import apply_discount, load_menu, save_sale, load_sales, daily_summary 

# Kasi Eats Stall Information
stall_name = "Kasi Eats" #str
owner_name = "Mama Thandi" #str
location = "Soweto" #str
VAT_RATE = 0.15 #float
is_open = True #bool

MENU = load_menu("data/menu.json")

items_on_menu = len(MENU) #int

def calculate_total(order, vat_rate):
    """Return (subtotal, discount, vat) for display; Order.total() gives the final number."""
    subtotal = 0
    for name, qty, line_total in order:
        subtotal += line_total

    discount = apply_discount(subtotal)
    taxable = subtotal - discount
    vat = taxable * vat_rate

    return subtotal, discount, vat

def show_menu(menu):
    """Print the menu with the prices, one item per line."""
    print("MENU")
    for item in menu.values():
        print(item)

def print_receipt(order, vat_rate):
    """Print item lines and totals; return the grand total."""
    print("RECEIPT")
    for name, qty, line_total in order.items:
        print(f"{name.title():<15}{qty:>3}      R {line_total:>6.2f}")

    subtotal, discount, vat = calculate_total(order.items, vat_rate)
    total = order.total(vat_rate)

    print(f"{'Subtotal':<15}{'':>3}      R {subtotal:>6.2f}")
    if discount > 0:
        print(f"{'Discount (10%)':<15}{'':>3}      R {discount:>6.2f}")
    print(f"{'VAT (15%)':<15}{'':>3}      R {vat:>6.2f}")
    print(f"{'TOTAL':<15}{'':>3}      R {total:>6.2f}")

    return total

def take_order(menu):
    """Collect items from the cashier; return an Order."""
    order = Order()

    while True:
        item = input("Item (or 'done'): ").strip().lower()

        if item == "done":
            break

        if item not in menu:
            print("Unknown item. Try again.")
            continue

        while True:
            try:
                qty = int(input("Quantity: "))
            except ValueError:
                print("Please enter a whole number.")
                continue
            if qty <= 0:
                print("Quantity must be a positive whole number.")
                continue
            break

        line_total = menu[item].price * qty
        order.add_item(item, qty, line_total)

    return order

# Main Program
def main():
    """Run the Kasi Eats order manager."""
    options = ["New Order", "View Menu", "Daily Summary", "Exit"]

    print("=" * 50)
    print(f"{stall_name} ORDER MANAGER - {location}".upper().center(50))
    print("=" * 50)

    cashier_name = input("Cashier name: ")
    print(f"Sawubona, {cashier_name}! Let's sell some kotas.")

    while True:
        print("MAIN MENU")
        for i, name in enumerate(options, 1):
            print(f"{i}. {name}")

        choice = input("Choose an option: ")

        if choice == "1":
            order = take_order(MENU)
            total = print_receipt(order, VAT_RATE)

            while True:
                try:
                    cash_paid = float(input("Cash paid: "))
                except ValueError:
                    print("Please enter a valid amount.")
                    continue
                if cash_paid < total:
                    print(f"Cash paid is less than total (R {total:.2f}).")
                    continue
                break

            change = cash_paid - total
            print(f"{'Change':<15}{'':>3}      R {change:>6.2f}")
            coins = change // 10
            remainder = change % 10
            print(f"({int(coins)} x R10 + R {remainder:.2f})")
            save_sale(order.items, total)

        elif choice == "2":
            show_menu(MENU)

        elif choice == "3":
            daily_summary()

        elif choice == "4":
            print("Sala kahle! Sales saved.")
            break

        else:
            print("Invalid option. Please choose 1 to 4.")


if __name__ == "__main__":
    main()