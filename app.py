from os import system
system ("cls")

from tax import calculateTax

salary = float(input(" Enter salary:" ))
interest = float(input(" Enter interest:" ))
tax = calculateTax(salary, interest, "salary")
print(tax)

print()