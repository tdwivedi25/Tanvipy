#buying stationery
#buying sticky notes
cost_of_sticknotes = eval(input("what is the cost of 1 pack-- "))
#buying pens
cost_of_5_pens = eval(input("what is the cost of 5 pens: "))
#buying notebooks
cost_of_10_notebooks = eval(input("what is the cost\t"))
#calculation of 3 items
subtotal = cost_of_sticknotes + cost_of_5_pens +cost_of_10_notebooks
#Calculation which includes sales tax
sales_tax = 0.08
total = cost_of_sticknotes + cost_of_5_pens + cost_of_10_notebooks + subtotal
print("The total cost is $",total)
print("This includes $", subtotal, "for the 3 items and")
print("$", sales_tax, "in sales tax.")

