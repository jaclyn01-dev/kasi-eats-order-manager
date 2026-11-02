# Kasi Eats Stall Information
stall_name = "Kasi Eats" #str
owner_name = "Mama Thandi" #str
location = "Soweto" #str
vat_rate = 0.15 #float
is_open = True #bool

#Menu Dictionary
MENU = {
    "kota": 35.00,
    "vetkoek": 12.50,
    "chips": 25.00,
    "cooldrink": 15.00,
    "samoosa": 8.00,
    "polony roll": 20.00,
}

items_on_menu = len(MENU) #int
items_sold_today = set()

def apply_discount(subtotal):
    """Return the discount amount: 10% of subtotal if subtotal is R200 or more, else 0."""
    if subtotal >= 200:
        return subtotal * 0.10
    return 0.0

def calculate_total(order, vat_rate):
    """Return (subtotal, discount, vat, total) for an order."""
    subtotal = 0
    for name, qty, line_total in order:
        subtotal += line_total

    discount = apply_discount(subtotal)
    taxable = subtotal - discount
    vat = taxable * vat_rate
    total = taxable + vat

    return subtotal, discount, vat, total


def show_menu(menu):
    """Print the menu with the prices, one item per line."""
    print("MENU")
    for name, price in menu.items():
        print(f"{name.title():<15} R {price:>6.2f}")

def print_receipt(order, vat_rate):
    """Print item lines and totals; return the grand total."""
    print("RECEIPT")
    for name, qty, line_total in order:
        print(f"{name.title():<15}{qty:>3}      R {line_total:>6.2f}")

    subtotal, discount, vat, total = calculate_total(order, vat_rate)

    print(f"{'Subtotal':<15}{'':>3}      R {subtotal:>6.2f}")
    if discount > 0:
        print(f"{'Discount (10%)':<15}{'':>3}      R {discount:>6.2f}")
    print(f"{'VAT (15%)':<15}{'':>3}      R {vat:>6.2f}")
    print(f"{'TOTAL':<15}{'':>3}      R {total:>6.2f}")

    return total

def take_order(menu):
    """Collect items from the cashier; return a list of (item, qty, line_total) tuples."""
    order = []
    while True:
        item = input("Item (or 'done'): ").strip().lower()

        if item == "done":
            break

        if item not in menu:
            print("Unknown item. Try again.")
            continue

        qty = int(input("Quantity: "))
        line_total = menu[item] * qty
        order.append((item, qty, line_total))

    return order

# Welcome Banner
print("=" * 50)
print(f"{stall_name} ORDER MANAGER - {location}".upper().center(50))
print("=" * 50)

#Variable Types
print(f"stall_name is {type(stall_name)}")
print(f"owner_name is {type(owner_name)}")
print(f"location is {type(location)}")
print(f"vat_rate is {type(vat_rate)}")
print(f"is_open is {type(is_open)}")
print(f"items_on_menu is {type(items_on_menu)}")

#Cashier Greeting
cashier_name = input("Cashier name: ")
print(f"Sawubona, {cashier_name}! Let's sell some kotas.")

#Main Menu Loop

options = ["New Order", "View Menu", "Daily Summary", "Exit"]

while True:
    print("MAIN MENU")
    for i, name in enumerate(options, 1):
        print(f"{i}. {name}")
    
    choice = input("Choose an option: ")

    if choice == "1":
        order = take_order(MENU)
        for name, qty, line_total in order:
            items_sold_today.add(name)

        total = print_receipt(order, vat_rate)

        cash_paid = float(input("Cash paid: "))
        change = cash_paid - total
        print(f"{'Change':<15}{'':>3}      R {change:>6.2f}")
        coins = change // 10
        remainder = change % 10
        print(f"({int(coins)} x R10 + R {remainder:.2f})")


    elif choice == "2":        
        show_menu(MENU)

    elif choice == "3":
        print("New order coming soon.")

    elif choice == "4":
        print("Sala kahle! Sales saved.")
        break

    else:
        print("Invalid option. Please choose 1 to 4.")