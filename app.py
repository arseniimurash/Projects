from os import system
system("cls")
from tax import *

purpose_of_payment = input("Write a purpose: ")
amount = float(input("How much money: "))
tax = float(input("Percent of tax: "))

n = purpose_of_payment
a = amount
t = tax

result = calculateTax(n,a,t)

system("cls")
for key, value in result.items():
    print(key, ':', value)
print()
