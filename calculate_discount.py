#Function to calculate Discount
def calculate_discount(price,discount_percentage):
     
    if discount_percentage>=20:
        discount_amount = (discount_percentage/100)*price
        discounted_price= price-discount_amount
        return discounted_price                                #Returns discounted price
    else:
        return price                                           #Returns original price since no discount is applied
    

  #Request User input on price and discount amount
price =float(input("ENTER THE ORIGINAL PRICE OF THE ITEM: "))
discount_percentage =float(input("ENTER DISCOUNT PERCENTAGE: "))

print(f'The Final price is :{calculate_discount(price,discount_percentage)}')





