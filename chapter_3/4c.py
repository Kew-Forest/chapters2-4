#Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#Write a loop that adds all the numbers from the list into a variable called total.
#You should set the total variable to have the value 0 before you start adding them up,
#and print the value in total after the loop has completed.


total = 0
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    total = total + i
print(total)    #301