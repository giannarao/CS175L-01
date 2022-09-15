#inputs
numberOfShares = 2000.00
purchasePrice = 40.00
commission = 0.03
salePrice = 42.75

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
