import turtle
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Hello, Alex!")      # Set the window title
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.color("blue") 

for i in range(4):
#for i in [0,1,2,3]:
    alex.forward(50)
    alex.left(90)
    
    