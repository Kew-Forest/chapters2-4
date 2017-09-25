"""
Write a Python program called “interest.py” that assigns the
principal amount of $10000 to variable P, assign to n the value 12,
and assign to r the interest rate of 8%. Then have the program prompt
the user for the number of years t that the money will be compounded for.
Calculate and print the final amount after t years.
"""
p = 10000
r = .08
n = 12
t = float(input("How many years are you investing for? "))
#t = float(t)
A = p * ( (1+r/n) ** (n*t) )
print("Your final amount after ",t," years will be: ", A)
