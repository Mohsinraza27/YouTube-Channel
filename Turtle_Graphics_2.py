import turtle
import random
x = turtle.Screen().bgcolor('black')

colors = ['green', 'yellow', 'magenta', 'red', 'orange', 'purple', 'blue', 'cyan']
t = turtle.Turtle()
t.speed(10)

for i in range(36):
    choice = random.choice(colors)
    t.pencolor(choice)
    t.forward(100)
    for _ in range(5):
        t.forward(30)
        t.right(360/5)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(10)
t.penup()
t.goto(0, -100)
t.pendown()
for i in range(50):
    t.pencolor('purple')
    t.circle(100+i, 45)