import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
sides = int(input("How many sides? "))
length = int(input("How long should each side be? "))

for i in range(sides):
    alex.forward(length)
    alex.left(360/sides)
    
#wn.mainloop()    