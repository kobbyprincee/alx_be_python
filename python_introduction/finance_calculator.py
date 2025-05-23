#Ask User for their income and expenses

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

#Calculate monthly savings

monthly_savings = monthly_income - monthly_expenses

#Project Annual savings with 5% interest

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Display the results

print("Your monthly savings are $",monthly_savings)
print("Projected Savings after one year,with interest,is $",projected_savings) 
