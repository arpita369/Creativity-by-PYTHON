import turtle
s = turtle.getscreen()
turtle.hideturtle()
t1 = turtle.Turtle()
s.title("Turtle moving as Fan")
t1.shape("turtle")
t1.pencolor("yellow")
t1.shapesize(10,10,10)
for angle in range (0, 9001, 90):
    t1.lt(angle)
input(0)