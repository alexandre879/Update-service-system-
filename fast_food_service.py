import random

class Menusystem:
    def __init__(self) -> None:
        self.menu = {
            1: {'food':'Pizza', 'price':3.50, 'quantity':20},
            2: {'food':'Burger', 'price':2.50, 'quantity':20},
            3: {'food':'Hotdog', 'price':1.50, 'quantity':20},
            4: {'food':'Frie', 'price':1.40, 'quantity':20},
            5: {'food':'Nuggets', 'price':1.80, 'quantity':20},
            6: {'food':'Cola', 'price':1.50, 'quantity':20},
            7: {'food':'Pepsi', 'price':1.40, 'quantity':20},
            8: {'food':'Sprite', 'price':1.40, 'quantity':20}
        }

        self.selected_items = []
        self.total_price = 0

#MENU_DISPLAY

    def display_menu(self) -> None:
        print('-Menu-')
        for key, item in self.menu.items():
            print(f'{key}) {item["food"]} - ${item["price"]:.2f} - (x{item["quantity"]} is available)')
        print('Press (0) to quit the menu')
        print('Press (S) to select the ordered items')
        print('Press (C) to clear the ordered items')
        print('Press (R) to random recommendiation')
        print('Press (P) to proceed to checkout')

#UPDATING_ITEMS_AFTER_CLEAR

    def update_quantity(self, food_item, quantity) -> None:
        for item in self.selected_items:
            if item['food'] == food_item:
                item['quantity'] += quantity
                break


#ORDERING_FOODS

    def order_food(self, choice) -> None:
        if choice in self.menu:
            selected_item = self.menu[choice]
            if selected_item['quantity'] > 0:
                print(f"available quantity: {selected_item['quantity']}")
                quantity = int(input(f'How many {selected_item["food"]} you want to order? '))
                if quantity < 1:
                    print('Please enter a valid quantities that is given in our menu')
                elif quantity > 20:
                    print('Sorry the reqeusted quantity is more then what is available in our menu system')
                else:
                    selected_item['quantity'] -= quantity
                    self.selected_items.append(selected_item)
                    self.total_price += selected_item['price'] * quantity
                    print(f"You have ordered x{quantity} {selected_item['food']} for each (${selected_item['price']:.2f}) available is (x{selected_item['quantity']} of {selected_item['food']})")

            else:
                print('Sorry the item is out of stock')

#SELECTION_OF_ORDERED_ITEMS

        
    def ordered_items(self) -> None:
        if len(self.selected_items) > 0:
            print('Here is the list of items that you selected:')
            item_count = {}
            for item in self.selected_items:
                food_name = item['food']
                item_count[food_name] = item_count.get(food_name, 0) + item['quantity']
                for item, quantity in item_count.items():
                    print(f"{item} - (x{quantity})")

            else:
                print('To select the ordered items you must order at least one item')

#CLEARING_ITEMS

    def clearing_items(self) -> None:
        clear_request = input('Are you sure that you want to clear the selected items? (Yes(1))/(No(2)): ')
        if clear_request == '1':
            if len(self.selected_items) > 0:
                for item in self.selected_items:
                    self.update_quantity(item['food'], item['quantity'])
                self.total_price = 0
                self.selected_items = []
                print('Menu cleared')

            else:
                print('To clear the ordered items you msut order at least one item')

        elif clear_request == '2':
            print('Menu not cleared')

        else:
            print('You must input number 1 or 2')

#RANDOM_SELECT

    def random_recommendation(self) -> None:
        available_items = [item for item in self.selected_items if item['quantity'] > 0]
        if available_items:
            random_item = random.choice(available_items)
            self.update_quantity(random_item['food'], -1)
            self.selected_items.append({'food':random_item['food'], 'quantity':1, 'price':random_item['price']})
            self.total_price += random_item['food']
            print(f"We are recommeding you a {random_item['food']} for a {random_item['price']:.2f}")

        else:
            print('Sorry, this pocket of item is out of stock')

#CHECKOUT

    def proceed_to_checkout(self) -> bool:
        checkout_request = input('Are you sure that you want to proceed to checkout? (Yes(1))/(No(2)): ')
        if checkout_request == '1':
            if len(self.selected_items) > 0:
                print('Proceeding to checkout..')
                print('You have ordered the following items:')
                for item in self.selected_items:
                    food_name = item['food']
                    food_quantity = item['quantity']
                    print(f"({food_name}) - (x{food_quantity})")
                print(f'Your total payable is ({self.total_price:.2f})')
                print('Thank you for using our menu system, visit us later, and Enjoy your meal :)')
                return True
            
            else:
                print('To proceed to checkout you must order at least one item')
                return False
            
        elif checkout_request == '2':
            print('Checkout cancelled')


        else:
            print('Please enter a number 1 or 2 otherwise request will not be completed')

#QUIT_THE_MENU
    
    def quit_menu(self) -> bool:
        exit_request = input('Are you sure that you want to quit the menu? (Yes(1))/(No(2)): ')
        if exit_request == '1':
            print('Menu cancelled, goodbye, have a nice day :)')
            return True
        
        elif exit_request == '2':
            print('Exit request cancelled')
        
        else:
            print('You must enter only nubmer 1 or 2; otherwise, the request will not be completed')
            return False


 #RUN       
    
    def run(self) -> None:
        while True:
            self.display_menu()
            choice = input('Choose which item you want to order: ')
            if choice.isdigit():
                choice = int(choice)
                if choice == 0:
                    self.quit_menu()
                    break
                elif choice > 7:
                    print('The number that you selected is our of our menu range')

                else:
                    self.order_food(choice)

            elif choice.lower() == 's':
                self.ordered_items()

            elif choice.lower() == 'c':
                self.clearing_items()

            elif choice.lower() == 'r':
                self.random_recommendation()

            elif choice.lower() == 'p':
                self.proceed_to_checkout()
                break

            elif choice.strip() == '':
                print('You have inputted emptiness, you must enter number or letters that is given in our menu system')

            else:
                print('Invalid input, please enter ony number or letters which exists in our menu system')

            
if __name__ == '__main__':
    system_menu = Menusystem()
    system_menu.run()