
#Enter EAN-13 article number: 5901230094938
#Article number is correct
#Article manufactured in Poland


ean13 = input("Enter EAN-13 article number: ")
    
if len(ean13) == 13 and ean13.isdigit():
    print("Article number is correct")
        
        # Check if the first 3 digits are "590" (indicating it's from Poland)
    if ean13[:3] == "590":
        print("Article manufactured in Poland")
else:
    print("Invalid article number")