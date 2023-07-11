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
    