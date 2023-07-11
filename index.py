class Zomato:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add(self, dish_id, dish_name, price):
        dish = {
            'dish_id': dish_id,
            'dish_name': dish_name,
            'price': price,
            'availability': True
        }
        self.menu.append(dish)
        print(f"Dish '{dish_name}' added to the menu.")

    def remove(self, dish_id):
        for dish in self.menu:
            if dish['dish_id'] == dish_id:
                self.menu.remove(dish)
                print(f"Dish with ID '{dish_id}' removed from the menu.")
                break
        else:
            print(f"No dish found with ID '{dish_id}' in the menu.")

    def update(self, dish_id, availability):
        for dish in self.menu:
            if dish['dish_id'] == dish_id:
                dish['availability'] = availability
                print(f"Dish availability updated. Dish ID: '{dish_id}', Availability: {availability}")
                break
        else:
            print(f"No dish found with ID '{dish_id}' in the menu.")       
   
    def take_order(self, customer_name, dish_ids):
        order = {
            'order_id': len(self.orders) + 1,
            'customer_name': customer_name,
            'dishes': []
        }
        for dish_id in dish_ids:
            dish = self.find_dish(dish_id)
            if dish:
                order['dishes'].append(dish)
                print(f"Dish '{dish['dish_name']}' added to the order.")
            else:
                print(f"No dish found with ID '{dish_id}' in the menu. Skipped.")
        self.orders.append(order)