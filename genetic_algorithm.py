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
        text_succ = turtle.Turtle()
        text_succ.hideturtle()
        text_succ.clear()
        text_succ.penup()
        text_succ.setposition(-40, 100)
        text_succ.write("성공",font=("Arial", 30, "normal"))


#텍스트
text_gen1 = turtle.Turtle()
text_gen1.penup()
text_gen1.setposition(-100,-170)
text_gen1.hideturtle()
text_gen1.write("Generation ", False, font=("Arial", 20, "normal"))




# 유전 알고리즘 해볼까


# 램덤으로 초기 유전값 생성 20인자씩 총 100개 도착하는데 가로세로 8칸이 최단거리


#(dna인자 개수, 개체 개수)
def create_random_DNA(dna_info_count, cnt):
    cnt_gen_list = []
    for i in range(cnt):
        gen_list = []
        for j in range(dna_info_count):
            gen_list.append(randint(1,4))
            
        cnt_gen_list.append(gen_list)

    return cnt_gen_list


# 랜덤인자들 실행후 최종값들 거리측정

def execute_measure_distance_of_DNA(cnt_lists):
    gen_distance = []
    count = 0
    for i in range(len(cnt_lists)):
        count += 1
        print(count)
        for j in range(20):
            gen_execute(cnt_lists[i], j)

        distance = math.sqrt(math.pow(p1.xcor()-f1.xcor(),2)+math.pow(p1.ycor()-f1.ycor(),2))
        gen_distance.append(distance)
        p1.setposition(-70, -70)

    return gen_distance




# 목적지와 가장 가까운값 5개 추출

def select_DNA(cnt_lists2, gen_distance2):
    selected_gen_list = []

    #가장 거리 가까운 인덱스값 리스트 5개
    for i in range(5):
        selected_gen_list.append( cnt_lists2[gen_distance2.index(min(gen_distance2))] )  

        gen_distance2[gen_distance2.index(min(gen_distance2))] = 1000


    for i in range(5):
        print(selected_gen_list[i])

    print("----------------------------------------")

    return selected_gen_list




# 두 값을 받아오고 랜덤 교차를 이용하여 다음세대 10마리 생산


def generate_next_gen(selected_gen_list2):
    second_100_gen_list = []

    for i in range(100):
        mixed_gen = []
        
        for j in range(20):
            mixed_gen.append(selected_gen_list2[randint(0,4)][j])

        second_100_gen_list.append(mixed_gen)

    return second_100_gen_list









TEST1 = create_random_DNA(20, 100)

generation = 0

text_gen2 = turtle.Turtle()
text_gen2.hideturtle()

for i in range(5):
    generation += 1


    text_gen2.clear()
    text_gen2.penup()
    text_gen2.setposition(60, -170)
    text_gen2.write(str(generation),font=("Arial", 20, "normal"))
    
    TEST2 = execute_measure_distance_of_DNA(TEST1)
    
    TEST3 = select_DNA(TEST1, TEST2)
    
    TEST1 = generate_next_gen(TEST3)




#### 돌연변이 추가해야 값도 여러개로 늘리기 받아오기.. 개수좀 늘리자















