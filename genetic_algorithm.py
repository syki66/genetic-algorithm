import turtle
import os
from random import randint
import math
import time


#배경
wn = turtle.Screen()
wn.setup(1290, 730)


#녹화할 시간좀 확보
wn.delay(100)

start = turtle.Turtle()
start.speed(1)
start.penup()
start.hideturtle()
start.setposition(300,300)


#창크기
wn.bgcolor("yellow")
wn.title("Gen turtle")

#wn.delay(0.05) # 가속
wn.delay(5)

#경계선
border_pen = turtle.Turtle()
border_pen.speed(5)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-200,-200)
border_pen.pendown()
border_pen.pensize(3)
border_pen.hideturtle()

for side in range(4):
    border_pen.fd(400)
    border_pen.lt(90)


#유전인자 경계선(-344 + (i*12), 178)
gen_border_pen = turtle.Turtle()
gen_border_pen.speed(0)
gen_border_pen.hideturtle()
gen_border_pen.color("black")
gen_border_pen.pensize(1)


for i in range(11):
    gen_border_pen.setheading(270)
    gen_border_pen.penup()
    gen_border_pen.setposition(-344 + (i*12), 178)
    gen_border_pen.pendown()
    gen_border_pen.fd(390)
    
for i in range(2):
    gen_border_pen.setheading(0)
    gen_border_pen.penup()
    gen_border_pen.setposition(-344,178-(390*i))
    gen_border_pen.pendown()
    gen_border_pen.fd(121)


#거북이
p1 = turtle.Turtle()
p1.color("blue")
p1.shape("turtle")
p1.penup()
p1.speed(0)
p1.setheading(90)
p1.setposition(-170, -170)
p1.shapesize(3, 3)
p1speed = 15 #거북이 한번에 이동거리 얼마로할지 조절

#먹이
f1 = turtle.Turtle()
f1.color("red")
f1.shape("circle")
f1.penup()
f1.speed(0)
f1.setheading(90)
f1.shapesize(1,1)
f1.setposition(170,170)
#f1.setposition(0,0)

#키조작
def move_left():
    p1.setheading(180)
    x = p1.xcor()
    x -= p1speed
    if x < -200:
        x = -200
    p1.setx(x)
    isCollision(f1,p1)

def move_right():
    p1.setheading(0)
    x = p1.xcor()
    x += p1speed
    if x > 200:
        x = 200
    p1.setx(x)
    isCollision(f1,p1)

def move_down():
    p1.setheading(270)
    y = p1.ycor()
    y -= p1speed
    if y < -200:
        y = -200
    p1.sety(y)
    isCollision(f1,p1)
        
def move_up():
    p1.setheading(90)
    y = p1.ycor()
    y += p1speed
    if y > 200:
        y = 200
    p1.sety(y)
    isCollision(f1,p1)


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

'''
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
'''

#거리만
def Distance(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    return distance

#충돌

generation_sucess_cnt = 0

text_succ = turtle.Turtle()
text_succ.hideturtle()
text_succ.penup()
text_succ.setposition(30, 200)
text_succ.write(str(generation_sucess_cnt),font=("Arial", 30, "normal"))

try_cnt = 0
is_count = 0
def isCollision(t1, t2):
    global try_cnt
    global is_count
    global generation_sucess_cnt
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))

    
    if ( (distance < 30) and (is_count != try_cnt) ):
        is_count = try_cnt #성공률 중복카운팅 방지

        generation_sucess_cnt += 1
              
        text_succ.clear()
        text_succ.penup()
        text_succ.setposition(30, 200)
        text_succ.write(str(generation_sucess_cnt)+"%",font=("Arial", 30, "normal"))


#텍스트
text_gen1 = turtle.Turtle()
text_gen1.penup()
text_gen1.setposition(-100,-240)
text_gen1.hideturtle()
text_gen1.write("Generation ", False, font=("Arial", 20, "normal"))

text_suc = turtle.Turtle()
text_suc.penup()
text_suc.setposition(-100,205)
text_suc.hideturtle()
text_suc.write("성공률 = ", False, font=("Arial", 20, "normal"))

#
text_suc.setposition(-342,-230)
text_suc.hideturtle()
text_suc.write("(up, down, left, right)", False, font=("Arial", 10, "normal"))


text_try = turtle.Turtle()
text_try.penup()
text_try.setposition(220,30)
text_try.hideturtle()
text_try.write("Try", False, font=("Arial", 20, "normal"))


text_try_count = turtle.Turtle()
text_try_count.penup()
text_try_count.setposition(230,-10)
text_try_count.hideturtle()


text_accel = turtle.Turtle()
text_accel.hideturtle()
text_accel.penup()
text_accel.setposition(210,-200)

gen_txt2 = turtle.Turtle()
gen_txt2.hideturtle()
gen_txt2.penup()
gen_txt2.setposition(-350, 210)
gen_txt2.write("상위 10% 유전자",font=("Arial", 14, "normal"))




# 유전 알고리즘 해볼까


# 램덤으로 초기 유전값 생성 20인자씩 총 100개 도착하는데 43칸이 최단거리


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
    global try_cnt
    try_cnt = 0
    
    gen_distance = []

    for i in range(len(cnt_lists)):
        text_try_count.clear()
        try_cnt += 1
        text_try_count.write(str(try_cnt), False, font=("Arial", 20, "normal"))

        if (try_cnt < 5):
            text_accel.clear()
            wn.delay(50)
            
        else :
            wn.delay(0.2)
            text_accel.write("X250", False, font=("Arial", 20, "bold"))
            
        for j in range(len(cnt_lists[0])):
            gen_execute(cnt_lists[i], j)

        distance = math.sqrt(math.pow(p1.xcor()-f1.xcor(),2)+math.pow(p1.ycor()-f1.ycor(),2))
        gen_distance.append(distance)
        p1.setposition(-170, -170)

    return gen_distance



gen_info = turtle.Turtle()
gen_info.hideturtle()
gen_info.penup()

gen_txt = turtle.Turtle()
gen_txt.hideturtle()
gen_txt.penup()




# 목적지와 가장 가까운값 10개 추출 (상위 10퍼)
generation_cnt = 0
def select_DNA(cnt_lists2, gen_distance2):
    global generation_cnt
    selected_gen_list = []

    #가장 거리 가까운 인덱스값 리스트 10개
    for i in range(10):
        selected_gen_list.append( cnt_lists2[gen_distance2.index(min(gen_distance2))] )  

        gen_distance2[gen_distance2.index(min(gen_distance2))] = 10000


    #유전자 정보 화면에 출력
    gen_info.clear()
    gen_txt.clear()
    generation_cnt += 1
    gen_txt.setposition(-350, 230)
    gen_txt.write(str((generation_cnt))+"세대",font=("Arial", 14, "normal"))

    for i in range(len(selected_gen_list)):
        gen_info.setposition(-340 + (i*12), 180)
        gen_info.write(str(i+1),font=("Arial", 10, "normal"))
        
        for j in range(len(selected_gen_list[1])):
            if (selected_gen_list[i][j] == 1):
                gen_info_text = "L"
            elif (selected_gen_list[i][j] == 2):
                gen_info_text = "U"
            elif (selected_gen_list[i][j] == 3):
                gen_info_text = "R"
            else:
                gen_info_text = "D"
            gen_info.setposition(-340 + (i*12), 165 - (j*9))
            gen_info.write(gen_info_text,font=("Arial", 8, "normal"))


    return selected_gen_list




# 두 값을 받아오고 랜덤 교차를 이용하여 다음세대 100마리 생산


def generate_next_gen(selected_gen_list2):
    second_100_gen_list = []

    for i in range(100):
        mixed_gen = []
        
        for j in range(len(selected_gen_list2[0])):
            mixed_gen.append(selected_gen_list2[randint(0,3)][j])

        second_100_gen_list.append(mixed_gen)

    return second_100_gen_list




#돌연변이 위치 상관없이 2% (4300개 중에 90개) 인자 랜덤으로 대입
def mutate_DNA(second_100_gen_list2, mutation_ratio):
    for i in range(mutation_ratio):
        second_100_gen_list2[randint(0,99)][randint(0,42)] = randint(1,4)

    return second_100_gen_list2




TEST1 = create_random_DNA(43, 100)

generation = 0

text_gen2 = turtle.Turtle()
text_gen2.hideturtle()

mutant_rate = 150
for i in range(16):
    
    generation += 1

    generation_sucess_cnt = 0
    text_succ.write("0",font=("Arial", 30, "normal"))

    text_gen2.clear()
    text_gen2.penup()
    text_gen2.setposition(60, -240)
    text_gen2.write(str(generation),font=("Arial", 20, "normal"))

    
    TEST2 = execute_measure_distance_of_DNA(TEST1)
    
    TEST3 = select_DNA(TEST1, TEST2)
    
    TEST4 = generate_next_gen(TEST3)

    TEST1 = mutate_DNA(TEST4, mutant_rate)

    mutant_rate -= 10

    time.sleep(1)

    text_succ.clear()