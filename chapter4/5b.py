import turtle
sn=turtle.Screen()
sn.bgcolor("lightgreen")
frank = turtle.Turtle()
frank.color("blue")
frank.pensize(3)

def draw_spiral(turt,sz,space,angle):
    """
    draws one spiral
    """
    for i in range(76):
        sz = sz + space
        turt.forward(sz)
        turt.right(angle)
draw_spiral(frank,5,5,91)    