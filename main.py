# including the fields: id, name, quantity (qty), and price.

from stock import Stock

total_stock= int(input(f"How much items do you want to add ?"))
for i in range(total_stock):
    A= input(f"Please Input {i+1} Items ID:  ")
    N= input(f"Please Input {i+1} Items name:  ")
    Q= input(f"Please Input {i+1} Items qty:  ")
    P= input(f"Please Input {i+1} Items rate:  ")

    k=Stock(id=A, name=N, quantity=Q, price=P)
    f=open("details.csv", "a")
    f.write(f"{k.id}, {k.name}, {k.quantity}, {k.price}\n")
    f.close()