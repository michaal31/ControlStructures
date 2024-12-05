# If more than 2 products are purchased, apply the discount

ammount = int(input("Number of products:  "))
price = float(input("Product price: "))
    
if ammount > 2:
    full_price = 2 * price
    discounted_price = (ammount - 2) * price * 0.75
    total_price = full_price + discounted_price
else:
        # No discount if 2 or fewer products are purchased
        total_price = ammount * price
    
print(f"Amount to pay: {total_price:.2f}")



