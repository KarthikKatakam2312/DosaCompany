import json
import argparse
import os
import itertools

def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        orders = json.load(file)
        return orders

def extractingdata(orders_data):
    for order in orders_data:
    #     name = order['name']
    #     phone = order['phone']
    #     print(f"Name extracted from order: {name}")
    #     print(f"Phone extracted from order: {phone}")
        add_customer(order['phone'],order['name'])
        items=itertools.chain.from_iterable((item['name'],item['price']) for item in order['items'])
        # print(list(items))
        for item in order["items"]:
            item_name = item["name"]
            items_info.setdefault(item_name, {"price": item["price"], "orders": 0})
            items_info[item_name]["orders"] += 1
    add_items(items_info)
    #    items = order['items']
    #     for item in items:
    #         # print(item)    
    #         itemname=item['name']
    #         itemprice=item['price']
    #         print(f"ItemName extracted from order: {itemname}")
    #         print(f"ItemPrice extracted from order: {itemprice}")
    #         add_items(itemname,itemprice)



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
     
def add_items(itemdata):
    file_path = "items.json"

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            itemdata = json.load(file)
    else:
        with open(file_path, 'w') as file:
            json.dump(itemdata, file, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Provide the Json File name')
    parser.add_argument('filename', type=str, help='Provide the filename containing json objects')

    args = parser.parse_args()
    orders_data = read_json_from_file(args.filename)
    items_info = {}


    if orders_data:
        print("Orders read successfully:")
        print(json.dumps(orders_data, indent=2))
        extractingdata(orders_data)
