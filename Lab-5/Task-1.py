total = 0
items = 0

print("CAMPUS CAFE MENU")
print("1. Coffee   - 25 SEK")
print("2. Sandwich - 45 SEK")
print("3. Cake     - 35 SEK")
print("0. Finish order")

while True:

    choice = input("Choice: ")

    if choice == "0":
        break

    elif choice == "1":
        print("Coffee: 25.00 SEK")
        total = total + 25
        items = items + 1

    elif choice == "2":
        print("Sandwich: 45.00 SEK")
        total = total + 45
        items = items + 1

    elif choice == "3":
        print("Cake: 35.00 SEK")
        total = total + 35
        items = items + 1

    else:
        print("Invalid choice.")

if total < 50:
    discount = 0

elif total < 100:
    discount = total * 0.05

else:
    discount = total * 0.10

final_total = total - discount

print("\nORDER SUMMARY")
print(f"Items: {items}")
print(f"Subtotal: {total:.2f} SEK")
print(f"Discount: {discount:.2f} SEK")
print(f"Total: {final_total:.2f} SEK")