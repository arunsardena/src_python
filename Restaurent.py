#Write a Python class Restaurant with attributes like menu items, book table, and customer orders, and methods like add_item_to_menu, book #tables, and customer order.
#Perform the following tasks now:
#Now add items to the menu.
#Make table reservations.
#Take customer orders.
#Print the menu.
#Print table reservations.
#Print customer orders.
#Note: Use dictionaries and lists to store the date.

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self,table_number, order):
        order_details = {'table_number': table_number, 'order': order}
        self.customer_orders.append(order_details)

    def print_menu_items(self):
        for item,price in self.menu_items.items():
            print("{} : {}".format(item,price))

    def print_table_reservations(self):
        for eachTable in self.book_table:
            print("Table:{}".format(eachTable))

    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))


r1 = Restaurant()

# Add items
r1.add_item_to_menu("Chicken Soup", 9.99)
r1.add_item_to_menu("Babycorn chilly", 8)
r1.add_item_to_menu("Grilled Fish", 19.99)
r1.add_item_to_menu("French Fries", 3.99)
r1.add_item_to_menu("Paneer grill", 15)

# Book table
r1.book_tables(1)
r1.book_tables(2)
r1.book_tables(3)
# Order items
r1.customer_order(1, "Chicken Soup")
r1.customer_order(1, "Grilled Fish")
r1.customer_order(2, "Paneer grill")
r1.customer_order(2, "French Fries")

print("\nPopular dishes in the restaurant along with their prices:")
r1.print_menu_items()
print("\nTable reserved in the Restaurant:")
r1.print_table_reservations()
print("\nPrint customer orders:")
r1.print_customer_orders()

