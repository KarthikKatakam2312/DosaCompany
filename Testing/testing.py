import json 
import os

file_path='example_orders.json'
dic={}

# def format_phone_number(phone_number):
#     digits = ''.join(c for c in phone_number if c.isdigit())

#     if len(digits) == 10:
#         return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"

#     return phone_number

# def is_valid_phone_number(phone_number):
#     return len(phone_number) == 12 and all(c.isdigit() for c in phone_number.replace("-", ""))

def add_customer(phone_number, customer_name):
    file_path = "customers.json"

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            customers_data = json.load(file)
    else:
        customers_data = {}
    customers_data[phone_number] = customer_name
    with open(file_path, 'w') as file:
        json.dump(customers_data, file, indent=4)


    print(f"Customer '{customer_name}' with phone number '{phone_number}' added successfully.")


def add_items(itemname, itemprice):
    file_path = "items.json"

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            item_data = json.load(file)
    else:
        item_data = {}
    item_data[itemname] = itemprice
    with open(file_path, 'w') as file:
        json.dump(item_data, file, indent=4)

with open(file_path, 'r') as file:
    orders = json.load(file)
for order in orders:
    name = order['name'] if 'name' in order else ''
    phone = order['phone'] if 'phone' in order else ''
    print(f"Name extracted from order: {name}")
    print(f"phone Number extracted from order: {phone}")
    # checkphone=is_valid_phone_number(phone)
    # print(checkphone)
    add_customer(phone,name)
    items = order['items']
    for item in items:
        # print(item)    
        itemname=item['name'] if 'name' in item else ''
        itemprice=item['price'] if 'name' in item else ''
        print(f"ItemName extracted from order: {itemname}")
        print(f"ItemPrice extracted from order: {itemprice}")
        add_items(itemname,itemprice)