menu=[]
def add(dish_id,dish_name,price,available)  :
    dish={
        "dish_id":dish_id,
        "dish_name":dish_name,
        "price":price,
        "availability":available
    }
    menu.append(dish)

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
    
        choice = input("Enter you choice: ")

        if choice == "1":
            dish_id = input("Enter Dish ID: ")
            dish_name = input("Enter dish name: ")
            price = input("Enter dish price: ")
            available = input("is dish available ? (yes/no): ")
            add(dish_id, dish_name, price, available)
if __name__ == "__main__":
    main()    