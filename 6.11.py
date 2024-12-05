
current = 140
previous = 200
    # Calculate the percentage decrease
price_decrease = ((previous - current) / previous) * 100
    
    # Check if the price decreased by at least 10%
if price_decrease >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_decrease:.0f}%")
else:
    print("Price has not decreased enough to recommend buying.")
    
