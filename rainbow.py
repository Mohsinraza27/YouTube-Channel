import turtle 

colors = ["red", "purple", "green"]

t = turtle.Turtle()
turtle.bgcolor("black")

for i in range(360):
    t.pencolor(colors[i%3])
    t.width(i/100 +1)
    t.forward(i)
    t.left(59)

turtle.done()
