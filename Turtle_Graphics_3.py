def drawspiral(how_for, how_much):
    if how_for>0:
        t.forward(how_for)
        t.right(how_much)
        drawspiral(how_for-5, how_much)

import turtle
turtle.Screen().bgcolor('black')
t= turtle.Turtle()
t.reset()
t.pencolor('green')
t.pen(speed=6)
turtle.delay(10)
length = 500
turn_by = 121
t.setpos(-length/2, length/2)
t.pendown()
drawspiral(length, turn_by)
