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
vat = subtotal * vat_rate #VAT is added on top of the menu prices, as in the project brief
total = subtotal + vat

print(f"Subtotal: R {subtotal:.2f}")
print(f"VAT: R {vat:.2f}")
print(f"Total: R {total:.2f}")

#Cash Paid and Change
cash_paid = float(input("Cash Paid: "))

change = cash_paid - total

print(f"Change: R {change:.2f}")

coins = change // 10
remainder = change % 10

print(f"R {change:.2f} ({int(coins)} x R 10 + R {remainder:.2f})")