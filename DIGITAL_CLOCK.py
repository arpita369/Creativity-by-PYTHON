from turtle import *
import turtle
import time

#make screen
s=turtle.getscreen()
s.bgcolor("pink")
s.setup(width=500, height=100)
s.cv._rootwindow.overrideredirect(1)

turtle.ht()
turtle.goto(0,-20)

#show time
while True:
    t=time.strftime("%H:%M:%S")
    turtle.write(t, font=("times new roman",30,"bold"), align="center")
    turtle.undo()
     
turtle.done()
 