import turtle
import random
import time


delay=0.1
score=0
highestscore=0
turtle.ht()

#snake bodies
bodies=[]


#make the screen
s=turtle.getscreen()
s.setup(width=600,height=600)
s.bgcolor("grey")
s.title("SNAKE GAME")


#snake head
head=turtle.Turtle()
head.shape("square")
head.color("white")
head.fillcolor("black")
head.penup()
head.goto(0,0)
head.direction="stop"


#snake food
food=turtle.Turtle()
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.speed(0)
food.pu()
food.ht()
food.goto(0,200)
food.st()


#score board
sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-290,-290)
sb.write(" SCORE: 0  |  HIGHEST SCORE: 0 ")


#movemnets
def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveright():
    if head.direction!="left":
        head.direction="right"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def movestop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)


#Event handling - key mappings
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveright,"Right")
s.onkey(moveleft,"Left")
s.onkey(movestop,"space")


#main loop
while True:
    s.update() #to update the screen
    #collison with border
    if head.xcor()>290:
        head.ht()
        head.setx(-290)
        head.speed(0)
        head.st()
    if head.xcor()<-290:
        head.ht()
        head.setx(290)
        head.speed(0)
        head.st()
    if head.ycor()>290:
        head.ht()
        head.sety(-290)
        head.speed(0)
        head.st()
    if head.ycor()<-290:
        head.ht()
        head.sety(290)
        head.speed(0)
        head.st()
    

    #collison with food
    if head.distance(food)<20:
        #change the position of the food
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #increase the length of the snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("black")
        body.fillcolor("red")
        bodies.append(body)

        #change delay
        delay-=0.001

        #increase the score
        score+=10

        #update the highest score
        if score>highestscore:
            highestscore=score
        sb.clear()
        sb.write(" SCORE: {}  |  HIGHEST SCORE: {} ".format(score,highestscore))
        

    #move the snake bodies
    for index in range (len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)


    #move the snake head
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

    #check collision in snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            delay=0.1

            #update score board
            sb.clear()
            sb.write(" SCORE: {}  |  HIGHEST SCORE: {} ".format(score,highestscore))
    time.sleep(delay)
s.mainloop()
#turtle.done()