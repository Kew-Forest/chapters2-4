import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
angle = -144
length = 100

for i in range(5):
    alex.forward(length)
    alex.left(angle)
alex.hideturtle()    
wn.mainloop() 