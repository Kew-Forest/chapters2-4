
import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Hello, Alex!")      # Set the window title
alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.color("blue")         # Set the attribute red
alex.pensize(3)
alex.speed(10)
colors = ["red","orange","blue","SeaGreen3"]
size = 200              #set the start size of the square
sizefactor = 1
for c in colors:              #the loop for colors    
    size = size/sizefactor      #we reduce the size
    sizefactor = sizefactor + 1 #we add one to the sizefactor each pass
    alex.color(c)
    for j in range(12):           #this loop makes 12 squares in a circle
        for i in range(4):                  #loop draws a square
            alex.forward(size)             # Make alex draw a square
            alex.left(90)
            #print(i)
        alex.left(30)
    alex.left(10)
wn.mainloop()             # Wait for user to close window    