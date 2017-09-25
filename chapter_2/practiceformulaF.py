"""
Write a Python program called “interest.py” that assigns the
principal amount of $10000 to variable P, assign to n the value 12,
and assign to r the interest rate of 8%.
Then have the program prompt the user for the number
of years t that the money will be compounded for.
Calculate and print the final amount after t years.
"""
P = 10000
n = 12
r = .08
t = int(input("years? "))

A = P * (1 + r/n) ** (n*t)

print("Your final amount is: ",A)
