order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
member = input("Is the customer a member? (yes/no): ").lower()

if requested_quantity <= 0:
    print("Order rejected: requested quantity must be greater than 0.")
elif requested_quantity > available_stock:
    print("Order rejected: insufficient stock.")
elif order_amount <= 0:
    print("Order rejected: order amount must be greater than 0.")
else:
    if member == "yes" and order_amount >= 500:
        final_price = order_amount * 0.90
        print("Order approved: member discount applied (10%).")
    elif member == "yes" and order_amount < 500:
        final_price = order_amount
        print("Order approved: member discount requires an order of at least 500 TRY.")
    else:
        final_price = order_amount
        print("Order approved: standard price applied.")

    print(f"Final price: {final_price:.2f} TRY")
