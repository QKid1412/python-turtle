## TOP LEVEL
import turtle as t
import random as r
import math as m

t.colormode(255)
t.bgcolor((100,50,200))


##Functions          
def rectangle(x,y):
    for i in range(2):
        t.forward(x)
        t.left(90)
        t.forward(y)
        t.left(90)
    return

def star(x):
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):
        t.forward(x)
        t.right(144)
    t.end_fill()
    return

def triangle(x):
    for i in range(3):
        t.forward(x)
        t.left(120)
    return

def shooting_star(x,y,z,w):
    position(x,y)
    t.left(230)
    t.pensize(1)
    t.pencolor("yellow")
    t.forward(z)
    t.penup()
    t.forward(40)
    t.pendown()
    star(w)
    t.right(230)
    return

def moon():
    t.pensize(3)
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(88,-360)
    t.end_fill()
    return

def random_col():
    x=r.randint(100,250)
    y=r.randint(180,250)
    z=r.randint(200,255)
    t.pencolor(x,y,z)
    t.fillcolor(z,x,y)
    return

def position(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    return

def move(x,y) :
    t.penup()
    t.left(x)
    t.forward(y)
    t.pendown()
    t.right(x)
    return

def arc(r,angle):
    arc_length = 2*m.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=float(angle)/n
    for i in range(n):
        t.forward(step_length)
        t.left(step_angle)

def petal(r, angle):
    for i in range(2):
        arc(r, angle)
        t.left(180-angle)
    
    
def flower(n, r, angle):
    random_col()
    t.begin_fill()
    for i in range(n):
        petal(r, angle)
        t.left(360.0/n)
    t.end_fill()

def window():
    t.pensize(3)
    t.pencolor("black")
    t.fillcolor("white")
    t.begin_fill()
    rectangle(20,20)
    t.end_fill()
    return
##TOP LEVEL

##Start drawing
t.speed(10)

##Stars with random positions and sizes (in certain ranges)
position(-225,265)
for i in range(5):
    x1=r.randint(25,40)
    x2=r.randint(25,40)
    y1=r.randint(30,50)
    y2=r.randint(30,50)
    z1=r.randint(60,85)
    z2=r.randint(60,85)
    star(x1)
    t.penup()
    t.right(y1)
    t.forward(z1)
    t.left(y1)
    t.pendown()
    star(x2)
    t.penup()
    t.left(y2)
    t.forward(z2)
    t.right(y2)

##The Moon    
position(-321,200)
moon()
##Several shooting stars
shooting_star(-200,150,150,30)
shooting_star(-140,150,210,45)
shooting_star(-60,150,270,55)

##The castle
position(100,-275)
t.pensize(3)
t.pencolor("black")
t.fillcolor("white")
t.begin_fill()
rectangle(150,160)
t.left(180)
t.forward(80)
t.right(180)
rectangle(80,100)
t.forward(230)
rectangle(80,100)
t.backward(120)
rectangle(90,100)
t.forward(45)
t.left(90)
t.forward(100)
t.backward(50)
t.penup()
t.left(90)
t.forward(10)
t.pendown()
t.circle(5,360)
t.penup()
t.setpos(190,-275)
t.right(90)
t.forward(45)
t.pendown()
t.circle(5,360)
t.end_fill()

position(88,-115)
t.fillcolor("white")
t.begin_fill()
t.right(90)
t.forward(172)
t.left(90)
t.forward(35)
for i in range(4):
    t.left(90)
    t.forward(22)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(16)
    t.right(90)
    t.forward(10)
t.left(90)
t.forward(20)
t.left(90)
t.forward(35)
t.end_fill()

position(124,-80)
t.fillcolor("white")
t.begin_fill()
t.left(180)
t.forward(45)
t.right(90)
t.forward(98)
t.right(90)
t.forward(45)
position(127,-80)
t.left(90)
for i in range(2):
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(16)
    t.left(90)
    t.forward(10)
    t.right(90)
t.end_fill()
t.fillcolor("white")
position(100,-35)
t.begin_fill()
triangle(150)
t.end_fill()

position(163,-70)
window()

position(10,-175)
t.fillcolor("white")
t.begin_fill()
t.forward(90)
t.left(90)
t.forward(22)
t.left(90)
for i in range(2):
    t.forward(20)
    t.right(90)
    t.forward(8)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(8)
    t.right(90)
t.left(90)
t.forward(22)
t.end_fill()

position(340,-175)
t.right(90)
t.fillcolor("white")
t.begin_fill()
t.forward(90)
t.right(90)
t.forward(22)
t.right(90)
for i in range(2):
    t.forward(20)
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(8)
    t.left(90)
t.right(90)
t.forward(22)
t.end_fill()

position(35,-145)
t.fillcolor("white")
t.begin_fill()
t.left(180)
t.forward(70)
t.right(90)
t.forward(45)
t.right(90)
t.forward(70)
t.right(90)
t.forward(25)
t.left(90)
t.forward(8)
t.right(90)
t.forward(20)
t.right(90)
t.forward(8)
t.end_fill()

position(65,-125)
window()

position(315,-145)
t.fillcolor("white")
t.begin_fill()
t.forward(70)
t.left(90)
t.forward(45)
t.left(90)
t.forward(70)
t.left(90)
t.forward(25)
t.right(90)
t.forward(8)
t.left(90)
t.forward(20)
t.left(90)
t.forward(8)
t.end_fill()

position(300,-125)
window()

position(20,-75)
t.right(90)
t.fillcolor("white")
t.begin_fill()
triangle(75)
t.end_fill()

position(255,-75)
t.fillcolor("white")
t.begin_fill()
triangle(75)
t.end_fill()

##Two flowers in random colors
##(learned from the website that Python Textbook recommanded)
position(-110,-140)
flower(6, 30.0, 90.0)
t.right(110)
t.pencolor("green")
t.pensize(3)
arc(180,45)
t.fillcolor("green")
t.begin_fill()
t.left(90)
petal(70,60)
t.end_fill()
t.left(80)
t.pencolor("green")
t.pensize(3)
t.fillcolor("green")
t.begin_fill()
petal(70,60)
t.end_fill()

t.right(120)
position(-220,-180)
flower(6, 25.0, 90.0)
t.right(100)
t.pencolor("green")
t.pensize(3)
arc(120,45)
t.fillcolor("green")
t.begin_fill()
t.left(90)
petal(50,60)
t.end_fill()
t.left(90)
t.pencolor("green")
t.pensize(3)
t.fillcolor("green")
t.begin_fill()
petal(55,60)
t.end_fill()

t.hideturtle()
##End of Program
