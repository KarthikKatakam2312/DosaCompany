import json
import argparse
import os
import itertools

items_info = {}

# Function to read JSON data from a file
def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        orders = json.load(file)
        return orders

# Function to extract data from jsonfile and update customer and item information
def extractingdata(orders_data):
    for order in orders_data:
        add_customer(order['phone'],order['name'])
        items=itertools.chain.from_iterable((item['name'],item['price']) for item in order['items'])
        for item in order["items"]:
            item_name = item["name"]
            items_info.setdefault(item_name, {"price": item["price"], "orders": 0})
            items_info[item_name]["orders"] += 1
    add_items(items_info)

# Function to add customer information to a JSON file
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
     
# Function to add item information to a JSON file
def add_items(itemdata):
    file_path = "items.json"

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            itemdata = json.load(file)
    else:
        with open(file_path, 'w') as file:
            json.dump(itemdata, file, indent=4)

# Main execution block
if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Provide the Json File name')
    parser.add_argument('filename', type=str, help='Provide the filename containing json objects')
    # Read orders data from the provided file
    args = parser.parse_args()
    orders_data = read_json_from_file(args.filename)
    if orders_data:
        # Extract and process data from orders
        extractingdata(orders_data)
