import turtle
import os
from random import randint
import math
import time


#배경
wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Gen turtle")

#경계선
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-100,-100)
border_pen.pendown()
border_pen.pensize(3)
border_pen.hideturtle()

for side in range(4):
    border_pen.fd(200)
    border_pen.lt(90)


#거북이
p1 = turtle.Turtle()
p1.color("blue")
p1.shape("turtle")
p1.penup()
p1.speed(0)
p1.setheading(90)
p1.setposition(-70, -70)
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
f1.setposition(70,70)

#키조작
def move_left():
    p1.setheading(180)
    x = p1.xcor()
    x -= p1speed
    if x < -100:
        x = -100
    p1.setx(x)
    if isCollision(f1,p1):
        print("목표달성")

def move_right():
    p1.setheading(0)
    x = p1.xcor()
    x += p1speed
    if x > 100:
        x = 100
    p1.setx(x)
    if isCollision(f1,p1):
        print("목표달성")

def move_down():
    p1.setheading(270)
    y = p1.ycor()
    y -= p1speed
    if y < -100:
        y = -100
    p1.sety(y)
    if isCollision(f1,p1):
        print("목표달성")
        
def move_up():
    p1.setheading(90)
    y = p1.ycor()
    y += p1speed
    if y > 100:
        y = 100
    p1.sety(y)
    if isCollision(f1,p1):
        print("목표달성")


#유전자 리스트 실행함수
def gen_execute(generationList, i):
    if generationList[i] == 1:
        move_left()
    elif generationList[i] == 2:
        move_up()
    elif generationList[i] == 3:
        move_right()
    else:
        move_down()


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
    
    if distance < 30:
        global count
        count = count + 1
        t1.clear()
        t1.write(str(count))
        t1.setposition(70,70)
        t1.write(str(count),font=("Arial", 30, "normal"))
        return True



#텍스트출력
t1 = turtle.Turtle()
t1.penup()
t1.setposition(100,300)
t1.hideturtle()
t1.write("Score = ", False, font=("Arial", 30, "normal"))




# 유전 알고리즘 해볼까


# 램덤으로 초기 유전값 생성 16인자씩 총 10개

ten_gen_list = []
for i in range(10):
    gen_list = []
    for j in range(16):
        gen_list.append(randint(1,4))
        
    ten_gen_list.append(gen_list)






# 랜덤인자들 실행후 최종값들 거리측정
gen_distance = []
for i in range(len(ten_gen_list)):
    for j in range(16):
        gen_execute(ten_gen_list[i], j)

    distance = math.sqrt(math.pow(p1.xcor()-f1.xcor(),2)+math.pow(p1.ycor()-f1.ycor(),2))
    gen_distance.append(distance)
    p1.setposition(-70, -70)








# 목적지와 가장 가까운값 두개 추출
selected_gen_list = []

selected_gen_list.append( ten_gen_list[gen_distance.index(min(gen_distance))] )  #가장 거리 가까운 인덱스값 리스트

gen_distance[gen_distance.index(min(gen_distance))] = 1000

selected_gen_list.append( ten_gen_list[gen_distance.index(min(gen_distance))] )  #두번째로 거리 가까운 인덱스값 리스트


print(selected_gen_list)






# 두 값을 이용해서 다음세대 10마리 생산

second_ten_gen_list = []

for i in range(10):
    mixed_gen = []
    
    for j in range(16):
        mixed_gen.append(selected_gen_list[randint(0,1)][j])

    second_ten_gen_list.append(mixed_gen)

for i in range(i):
    print(second_ten_gen_list[i])



















