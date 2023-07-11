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

    def find_dish(self, dish_id):
        for dish in self.menu:
            if dish['dish_id'] == dish_id and dish['availability']:
                return dish
        return None    
    def update_order(self, order_id, status):
        for order in self.orders:
            if order['order_id'] == order_id:
                order['status'] = status
                print(f"Order ID '{order_id}' updated. New status: {status}")
                break
        else:
            print(f"No order found with ID '{order_id}'.")

    def review_orders(self):
        if not self.orders:
            print("No orders to review.")
        else:
            print("Reviewing all orders:")
            for order in self.orders:
                print(f"Order ID: {order['order_id']}, Customer: {order['customer_name']}, Status: {order.get('status', 'N/A')}")

                