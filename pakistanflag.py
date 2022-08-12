import turtle

pk = turtle.Screen()
pk.bgcolor('black')
t = turtle.Turtle()
t.speed(5)
t.penup()
t.shape("turtle")

def rectangle(x, y, length, width, color):
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.end_fill()
    t.penup()

def star(x, y, color, length):
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for turn in range(0, 5):
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.penup()

def circle(x, y, color, radius):
    t.goto(x, y)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def moon(x, y, color, radius):
    t.up()
    t.goto(x, y)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_green():
    x = -230
    y = 125
    color = 'darkgreen'
    rectangle(x, y, 280, 460, color)

def draw_white():
    x = -230
    y = 125
    color = 'white'
    rectangle(x, y, 280, 130, color)

def draw_star():
    x = 70
    y = 30
    color = 'white'
    star(x, y, color, 50)

def draw_circle():
    x = 45
    y = -100
    color = 'white'
    circle(x, y, color, 80)

def draw_moon():
    x = 65
    y = -72
    color = 'dark green'
    moon(x, y, color, 70)

draw_green()
draw_white()
draw_circle()
draw_moon()
draw_star()

t.goto(125, -200)
t.color('green')
t.back(20)

t.pencolor('white')
t.penup()
t.goto(-220, 125)
t.pendown()
t.pensize(14)
t.write('Pakistan Zinda Bad', font=('Anteb Bold', 36, 'bold'))
t.hideturtle()

t.pencolor('green')
t.penup()
t.goto(-275, -210)
t.pendown()
t.pensize(14)
t.write('Happy Independence Day', font=('Anteb Bold', 36, 'bold'))
t.hideturtle()

turtle.done()



