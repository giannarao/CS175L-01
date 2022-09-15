#inputs
#numberOfShares = 2000.00
#purchasePrice = 40.00
#commission = 0.03
#salePrice = 42.75

numberOfShares = float(input("Enter the number of shares: "))
purchasePrice = float(input("Enter the purchase price: "))
commission = float(input("Enter the commission rate: "))
salePrice = float(input("Enter the sale price: "))

#calculations
amountPaid = numberOfShares * purchasePrice
commissionPaid = amountPaid * commission
totalSale = salePrice * numberOfShares
commissionSale = totalSale * commission
profit = totalSale - (amountPaid + commissionPaid + commissionSale)

#print
print("Amount paid for the stock:", f"${amountPaid:,.2f}")
print("Commisson paid on the purchase:", f"${commissionPaid:,.2f}")
print("Amount the stock sold for:", f"${totalSale:,.2f}")
print("Commission paid on the sale:", f"${commissionSale:,.2f}")
print("Profit (or loss if negative) :", f"${profit:,.2f}")
