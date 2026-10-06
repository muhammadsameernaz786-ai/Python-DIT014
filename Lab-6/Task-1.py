def show_products():
    print("\nAVAILABLE PRODUCTS")
    print("1. Notebook - 40.00 SEK")
    print("2. Mug - 60.00 SEK")
    print("3. Tote bag - 80.00 SEK")


def make_order():
    subtotal = 0
    discount = 0
    items = 0

    print("\nMAKE AN ORDER")
    print("Enter 0 when you are finished ordering.")

    product = input("Product: ")

    while product != "0":

        if product == "1":
            price = 40
            name = "Notebook"

        elif product == "2":
            price = 60
            name = "Mug"

        elif product == "3":
            price = 80
            name = "Tote bag"

        else:
            print("Invalid product.")
            product = input("Product: ")
            continue

        quantity = int(input("Quantity: "))

        if quantity < 1:
            print("Quantity must be at least 1.")

        else:
            item_subtotal = price * quantity
            item_discount = 0

            if quantity >= 5:
                item_discount = item_subtotal * 0.10

            item_total = item_subtotal - item_discount

            subtotal = subtotal + item_subtotal
            discount = discount + item_discount
            items = items + quantity

            print(f"{name} x{quantity}: {item_total:.2f} SEK")

        product = input("Product: ")

    return subtotal, discount, items


def finish_order(subtotal, discount, items):
    total = subtotal - discount

    print("\nLANTERN POP-UP RETAIL")
    print(f"Items: {items}")
    print(f"Subtotal: {subtotal:.2f} SEK")
    print(f"Discount: {discount:.2f} SEK")
    print(f"Total: {total:.2f} SEK")
    print("Thank you!")


def main():
    subtotal = 0
    discount = 0
    items = 0
    choice = ""

    while choice != "3":

        print("\nLANTERN POP-UP RETAIL")
        print("1. View products")
        print("2. Make an order")
        print("3. Finish")

        choice = input("Choice: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            order_subtotal, order_discount, order_items = make_order()

            subtotal = subtotal + order_subtotal
            discount = discount + order_discount
            items = items + order_items

        elif choice == "3":
            finish_order(subtotal, discount, items)

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()