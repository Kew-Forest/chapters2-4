#objects methods attributes

import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Hello, Alex!")      # Set the window title
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.color("blue")         # Set the attribute red
alex.pensize(3)
alex.speed(10)
alex.left(3645)
alex.forward(50)          # Tell alex to move forward by 50 units
#alex.left(120)             # Tell alex to turn by 120 degrees
#alex.forward(50)          # C

wn.mainloop()             # Wait for user to close window