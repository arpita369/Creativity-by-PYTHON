import turtle
s= turtle.getscreen()
turtle.ht()
t1=turtle.Turtle()
turtle.bgcolor("black")
t1.pencolor("red")
t1.fillcolor("yellow")
t1.shape("circle")
t1.shapesize(5,5,2)
t1.speed(100)
t1.penup()
x,y=0,300
t1.goto(x,y)
t1.stamp()
for r in range (100,0,-1):
        t1.rt(15)
        t1.fd(r)
        t1.stamp()
input()