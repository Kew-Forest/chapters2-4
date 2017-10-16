import turtle
wn=turtle.Screen()
jo = turtle.Turtle()

def make_star(turt):
    for i in range(5):
        turt.forward(100)
        turt.right(144)
        

for i in range(5):
    make_star(jo)
    jo.forward(350)
    jo.right(144)
    
    