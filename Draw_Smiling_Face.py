import turtle
import colorsys

screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)

# turtle object
t = turtle.Turtle()

# function for creation of eye
def eye(col, rad):
    t.down()
    t.fillcolor(col)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    t.up()

# draw face
t.fillcolor('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()
t.up()

#draw eyes
t.goto(-40, 120)
eye('white', 15)
t.goto(-37, 125)
eye('black', 5)
t.goto(40, 120)
eye('white', 15)
t.goto(40, 125)
eye('black', 5)

# draw nose
t.goto(0, 75)
eye('black', 8)

# draw mouth
t.goto(-40, 85)
t.down()
t.right(90)
t.circle(40, 180)
t.up()

# draw tongue
t.goto(-10, 45)
t.down()
t.right(180)
t.fillcolor('red')
t.begin_fill()
t.circle(10, 180)
t.end_fill()
t.hideturtle()
input()
turtle.done()

