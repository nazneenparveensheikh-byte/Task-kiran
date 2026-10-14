# Calculate Electronics bill with 18% GST
def calculateElectronicsGST(a, b):
    total = a + b
    return total + (total * 18 / 100)


# Calculate Fashion bill with 13% GST
def calculateFashionGST(c, d):
    total = c + d
    return total + (total * 13 / 100)


# Calculate Food bill with 7% GST
def calculateFoodGST(e):
    return e + (e * 7 / 100)


# Calculate total bill after GST
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


# Calculate final bill after 20% discount
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100

    return total - discount


# Sample test values
a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print("===== SHOPPING BILL =====")

print(f"Electronics after GST: {electronics:.2f}")
print(f"Fashion after GST:     {fashion:.2f}")
print(f"Food after GST:         {food:.2f}")

print("-------------------------")

print(f"Total after GST:        {total:.2f}")
print(f"20% Discount:           {discount:.2f}")
print(f"Final Payable Amount:   {final_amount:.2f}")
