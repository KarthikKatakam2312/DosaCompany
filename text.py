import json 

file_path='example_orders.json'
file_path = "customers.json"
with open(file_path, 'r') as file:
    orders = json.load(file)

for i in orders:

# print(type(orders))
    print(i["name"])
    print(i["phone"])

if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            customers_data = json.load(file)
    else:
        customers_data = {}
    customers_data[phone_number] = customer_name
    with open(file_path, 'w') as file:
        json.dump(customers_data, file, indent=4)