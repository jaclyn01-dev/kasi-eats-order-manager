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

print(f"stall_name is {type(stall_name)}")
print(f"owner_name is {type(owner_name)}")
print(f"location is {type(location)}")
print(f"vat_rate is {type(vat_rate)}")
print(f"is_open is {type(is_open)}")
print(f"items_on_menu is {type(items_on_menu)}")

cashier_name = input("Cashier name: ")
print(f"Sawubona, {cashier_name}! Let's sell some kotas.")