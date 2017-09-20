
import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Hello, Alex!")      # Set the window title
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.color("blue")         # Set the attribute red
alex.pensize(3)
alex.speed(10)
colors = ["red","orange","blue","SeaGreen3"]
for c in colors:
    alex.color(c)
    for j in range(12):
        for i in range(4):
            alex.forward(50)             # Make alex draw a square
            alex.left(90)
            print(i)
        alex.left(30)
    alex.left(10)
wn.mainloop()             # Wait for user to close window    