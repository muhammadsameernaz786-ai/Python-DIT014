table = int(input("enter your table number : "))
client = input("enter your name : ")

prd_1 = input("enter your first product : ")
price_1 = float(input("enter your price in sek : "))

prd_2 = input("enter your second product : ")
price_2 = int(input("enter your price in sek : "))

prd_3 = input("enter your third product : ")
price_3 = float(input("enter your price in sek : "))

total = price_1 + price_2 + price_3 

print("JUNIPER CAFE COLLECTIVE")
print(table)
print(client)

print(f"{prd_1:.<24}   {price_1:.2f}sek")
print(f"{prd_2:.<24}   {price_2:.2f}sek")
print(f"{prd_3:.<24}   {price_3:.2f}sek")

print(f"Subtotal = {total}sek")