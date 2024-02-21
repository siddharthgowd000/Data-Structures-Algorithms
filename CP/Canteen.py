def canteen_init(items):
    global items_global  
    items_global = items

def print_menu():
    
    for i, item in enumerate(items_global):
        item_name = item['name'].capitalize()
        brand_name = item['brand'].capitalize()
        price = item['price']
        print(f"{i+1}. {item_name} ({brand_name}) - Rs.{price}")
    print("------------------------")
canteen_init([
    {"name": "tea", "price": 10,  "brand": "Lipton"},
    {"name": "coffee", "price": 20, "brand": "Nescafe"},
    {"name": "poha", "price": 40,  "brand": "Homemade"},
    {"name": "pepsi", "price": 20,  "brand": "Pepsi"},
    {"name": "laptop", "price": 10,  "brand": "macbook"}
])

print_menu()
s = "sahvhas@gmail.com"
print(s[-10:])