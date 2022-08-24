from turtle import *
import turtle

speed(8)
hideturtle()
width(4)

def rel_posi(x, y):
    penup()
    goto(pos()+(x, y))
    pendown()

def draw_roof():
    width(8)
    begin_fill()
    fillcolor('#cc6600')
    seth(180)
    forward(200)
    seth(-120)
    forward(100)
    seth(0)
    forward(200)
    end_fill()
    seth(60)
    forward(100)
    seth(-60)
    forward(100)
    width(4)
    seth(180)
    forward(100)

def draw_walls():
    seth(-90)
    forward(120)
    seth(180)
    forward(200)
    seth(90)
    forward(120)
    seth(0)
    forward(300)
    seth(-90)
    forward(120)
    seth(180)
    forward(100)
    
def draw_door():
    color('#004080')
    width(5)
    forward(80)
    begin_fill()
    fillcolor('red')
    seth(90)
    forward(80)
    seth(180)
    forward(40)
    seth(-90)
    forward(80)
    end_fill()
    rel_posi(25, 40)
    width(4)
    circle(5)

def draw_windows():
    begin_fill()
    color('#004080')
    fillcolor('#336699')
    seth(-90)
    width(5)
    forward(15)
    seth(180)
    forward(30)
    seth(90)
    forward(30)
    seth(0)
    forward(30)
    seth(-90)
    forward(15)
    end_fill()
    width(2)
    seth(180)
    forward(30)
    backward(15)
    seth(90)
    forward(15)
    backward(30)

def write_text():
    speed(5)
    color('#009900')
    write('''    Please Like the video 
    Subscribe to my Channel''', font=('Anton',22,"bold"))
    
def draw_House():
    draw_roof()
    draw_walls()
    draw_door()
    rel_posi(-50, 0)
    draw_windows()
    rel_posi(135, 15)
    draw_windows()
    rel_posi(105, 25)
    draw_windows()
    rel_posi(-250, 250)
    write_text()
    done()

draw_House()

    



  

