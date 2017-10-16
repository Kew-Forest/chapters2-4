import turtle
wn = turtle.Screen()
jo = turtle.Turtle()

def draw_star(turt):
    for i in range(5):
        turt.forward(100)
        turt.right(144)
    #return turt.pos()
#print(draw_star(jo))

for i in range(5):
    draw_star(jo)
    jo.forward(350)
    jo.right(144)

