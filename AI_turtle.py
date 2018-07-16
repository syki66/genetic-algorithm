import turtle
import os
from random import randint
import math
import time


#배경
wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("AI turtle")

#경계선
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
border_pen.hideturtle()

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)


#거북이
p1 = turtle.Turtle()
p1.color("blue")
p1.shape("turtle")
p1.penup()
p1.speed(0)
p1.setheading(90)
p1.shapesize(3, 3)
p1speed = 15

#먹이
f1 = turtle.Turtle()
f1.color("red")
f1.shape("circle")
f1.penup()
f1.speed(0)
f1.setheading(90)
f1.shapesize(1,1)
f1.setposition(randint(-270,270),randint(-270,270))

#키조작
def move_left():
    p1.setheading(180)
    x = p1.xcor()
    x -= p1speed
    if x < -280:
        x = -280
    p1.setx(x)
    if isCollision(f1,p1):
        f1.setposition(randint(-270,270),randint(-270,270))

def move_right():
    p1.setheading(0)
    x = p1.xcor()
    x += p1speed
    if x > 280:
        x = 280
    p1.setx(x)
    if isCollision(f1,p1):
        f1.setposition(randint(-270,270),randint(-270,270))

def move_down():
    p1.setheading(270)
    y = p1.ycor()
    y -= p1speed
    if y < -280:
        y = -280
    p1.sety(y)
    if isCollision(f1,p1):
        f1.setposition(randint(-270,270),randint(-270,270))
        
def move_up():
    p1.setheading(90)
    y = p1.ycor()
    y += p1speed
    if y > 280:
        y = 280
    p1.sety(y)
    if isCollision(f1,p1):
        f1.setposition(randint(-270,270),randint(-270,270))

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
#거리만
def Distance(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    return distance

#충돌
count = 0
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    print(distance)
    if distance < 30:
        global count
        count = count + 1
        t1.clear()
        t1.write(str(count))
        t1.setposition(250,300)
        t1.write(str(count),font=("Arial", 30, "normal"))
        return True

#텍스트출력
t1 = turtle.Turtle()
t1.penup()
t1.setposition(100,300)
t1.hideturtle()
t1.write("Score = ", False, font=("Arial", 30, "normal"))

#시간
t2 = turtle.Turtle()
t2.penup()
t2.setposition(-300,300)
t2.hideturtle()

time1=time.time()
while True:
    t2.clear()
    t2.write(round((time.time()-time1),2), False, font=("Arial", 30, "normal"))




#인공지능

    Distance(p1,f1)
    
    ud_rand = randint(1,2)
    
    if ud_rand == 1:
        d1 = Distance(p1,f1)
        move_up()
        d2 = Distance(p1,f1)
        if d1<d2:
            move_down()
            move_down()
            move_down()
    else:
        d1 = Distance(p1,f1)
        move_down()
        d2 = Distance(p1,f1)
        if d1<d2:
            move_up()
            move_up()
            move_up()

        
    lr_rand = randint(1,2)
    if lr_rand == 1:
        d1 = Distance(p1,f1)
        move_left()
        d2 = Distance(p1,f1)
        if d1<d2:
            move_right()
            move_right()
            move_right()
    else:
        d1 = Distance(p1,f1)
        move_right()
        d2 = Distance(p1,f1)
        if d1<d2:
            move_left()
            move_left()
            move_left()
'''
while True:
    rand = randint(1,4)
    if rand == 1:
        move_up()
    elif rand == 2:
        move_down()
    elif rand == 3:
        move_left()
    else:
        move_right()'''
