from uuid import uuid4
menu=[]
orders=[]
def add(dish_id,dish_name,price,available)  :
    dish={
        "dish_id":dish_id,
        "dish_name":dish_name,
        "price":price,
        "availability":available
    }
    menu.append(dish)
    print(menu)

def remove(dish_id):
    for item in menu:
        if item["dish_id"] == dish_id:
            menu.remove(item)
            break
        else:
            print("item not found")

def update(dish_id,available):
    for item in menu:
        if item["dish_id"] == dish_id:
            item["availability"] = available
            break
        else:
            print("item not found")

def generate_id():
    return str(uuid4())

def take_order(customer_name,dish_id,quantity,order_id):
    for item in menu:
        if item["dish_id"] == dish_id:
            order={
                "customer_name":customer_name,
                "dish_id":dish_id,
                "quantity":quantity,
                "status":"received",
                "order_id":order_id
            }
            print(f"order created with ${order.order_id}")
            orders.append(order)
            print(orders)
        else:
            print("item not found,order something else")    

def update_status(order_id,status):
    for item in orders:
        if item["order_id"] == order_id:
            item["status"] = status
            break
        else:
            print("order not found")

#main loop
def main():
    while True:
        print(f"\nwelcome to Zesty Zomato")
        print("what you would like to do")
        print("1. Add a dish to your menu")
        print("2. Remove a dish from your menu")
        print("3. Update the availability of dish")
        print("4. Take new order")
        print("5. Update the status of an order")
        print("6. Review all orders")
        print("7. Exit")
        choice = input("Enter you choice: ")

        if choice == "1":
            dish_id = input("Enter Dish ID: ")
            dish_name = input("Enter dish name: ")
            price = input("Enter dish price: ")
            available = input("is dish available ? (yes/no): ")
            add(dish_id, dish_name, price, available)
        elif choice == "2":
            dish_id = input("Enter dish ID: ")
            remove(dish_id)    
        elif choice == "3":
            dish_id = input("Enter dish ID: ")
            available = input("is dish available ? (yes/no): ")
            update(dish_id,available)  
        elif choice == "4":
            customer_name = input("Enter customer name: ")
            dish_id = input("Enter dish ID: ")
            quantity = input("Enter dish quantity: ")
            order_id = generate_id()
            take_order(customer_name,dish_id,quantity,order_id)
        elif choice == "5":
            order_id = input("Enter order ID: ")
            status = input("Enter status: ")
            update_status(order_id,status)
        elif choice == "6":

        elif choice == "7":
            break
        else: 
            print("Invalid choice.Please try again.")  


if __name__ == "__main__":
    main()    