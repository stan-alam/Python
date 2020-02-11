orders = [("burger", 2, 5), ("fries", 4.2, 0), ("Bepsi", 1.75, 3)]

print("Product Quantity price Subtotal")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(
            f"{product:10s}{quantity: ^9d} "
            f"${price: <8.2}${subtotal: >7.2f}"
         )

