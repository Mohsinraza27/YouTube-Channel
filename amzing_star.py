import turtle

screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)

t=turtle.Turtle()
screen.bgcolor("black")
t.speed(10)

color = ['green', 'yellow', 'purple', 'blue', 'cyan']
c = 0

for i in range(80):
    t.forward(i * 7)
    t.right(144)
    t.color(color[c])
    if c == 3:
        c = 0
    else:
        c += 1
    
