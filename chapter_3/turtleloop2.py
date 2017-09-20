import turtle
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Hello, Alex!")      # Set the window title
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.color("blue")
alex.speed(10)

colors=["blue","red","green","purple","AliceBlue","CornflowerBlue","OrangeRed4"]
for j in colors:
    alex.color(j)
    for i in range(4):
        alex.forward(50)
        alex.left(90)
    alex.left(10)    