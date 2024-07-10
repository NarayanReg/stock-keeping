# Write a program that saves the details of 10 products to 
# a file using user input, 
# including the fields: id, name, quantity (qty), and price.


class Stock:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def display(self):
        print(f"Id: {self.id}, name: {self.name}, Qty: {self.quantity}, price: {self.price}")

    
