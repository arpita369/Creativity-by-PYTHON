import turtle
s= turtle.getscreen()
turtle.ht()
t1=turtle.Turtle()
t1.ht()
turtle.bgcolor("black")
t1.pencolor("red")
t1.fillcolor("yellow")
t1.shape("arrow")
t1.shapesize(1,1,1)
t1.speed(1000)
tc=["goldenrod","red","blue","white","darkgreen","darkviolet"]
for r in range (500):
        t1.lt(59)
        t1.fd(r)
        t1.pencolor(tc[r%6])      
input()