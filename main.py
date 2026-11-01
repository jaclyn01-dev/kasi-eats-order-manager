# Kasi Eats Stall Information
stall_name = "Kasi Eats" #str
owner_name = "Mama Thandi" #str
location = "Soweto" #str
vat_rate = 0.15 #float
is_open = True #bool
items_on_menu = 6 #int

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

# Price and Quantity
price = float(input("How much is the item? "))
quantity = int(input("How many units ordered? "))

print(f"{quantity} units ordered at R {price:.2f} per unit.")

#Subtotal, VAT and Total
subtotal = price * quantity

#Discount
discount = 0.0
if subtotal >= 200:
    discount = subtotal * 0.10

taxable = subtotal - discount
vat = taxable * vat_rate # Discount applied before VAT, so customer is taxed only on the discounted amount
total = taxable + vat

print(f"Subtotal: R {subtotal:.2f}")

if discount > 0:
    print(f"Discount (10%): R {discount:.2f}")

print(f"VAT: R {vat:.2f}")
print(f"Total: R {total:.2f}")

#Cash Paid and Change
cash_paid = float(input("Cash Paid: "))

change = cash_paid - total

print(f"Change: R {change:.2f}")

coins = change // 10
remainder = change % 10

print(f"R {change:.2f} ({int(coins)} x R 10 + R {remainder:.2f})")

#Main Menu Loop

options = ["New Order", "View Menu", "Daily Summary", "Exit"]

while True:
    print("MAIN MENU")
    for i, name in enumerate(options, 1):
        print(f"{i}. {name}")
    
    choice = input("Choose an option: ")

    if choice == "1":
        print("New order coming soon.")

    elif choice == "2":
        print("New order coming soon.")

    elif choice == "3":
        print("New order coming soon.")

    elif choice == "4":
        print("Sala kahle! Sales saved.")
        break

    else:
        print("Invalid option. Please choose 1 to 4.")