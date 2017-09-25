import turtle
wn = turtle.Screen()
pirate = turtle.Turtle()
steps = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in steps:
    pirate.left(i)
    pirate.forward(100)
    
    
wn.mainloop()    