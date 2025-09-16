# order_amount = float(input('Enter the order amount: '))
# if order_amount > 300:
#     print("Delivery is free on this product")
# else:
#     print("Delivery charge of Rs 30 is")

order_amount = float(input('Enter the order amount: '))

delivery_charge = 0 if order_amount > 300 else 30
print(f"Delivery charge is: {delivery_charge}")
