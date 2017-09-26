import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen") 
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(3)

alex.shape("turtle")
alex.stamp()
for i in range(12):
    alex.penup()
    alex.forward(150)
    alex.pendown()
    alex.forward(20)
    alex.penup()
    alex.forward(20)
    alex.stamp()
    alex.setpos(0,0)
    alex.left(360/12)
alex.hideturtle()

