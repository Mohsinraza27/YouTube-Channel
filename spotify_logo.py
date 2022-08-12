import turtle as t

t.begin_fill()
t.fillcolor('#1DB954')
t.circle(100)
t.end_fill()

t.penup()
t.goto(30, 40)
t.pendown()
t.left(130)
t.forward(0)
t.pensize(15)
t.pencolor('black')
t.circle(90, 60)

t.penup()
t.goto(40, 65)
t.pendown()
t.pensize(18)
t.right(60)
t.forward(0)
t.circle(100, 60)

t.penup()
t.goto(60, 95)
t.pendown()
t.pensize(20)
t.right(60)
t.forward(0)
t.circle(110, 60)

t.pencolor('black')
t.penup()
t.goto(100, 40)
t.pendown()
t.pensize(14)
t.write('Spotify', font=('Anteb Bold', 70, 'bold'))
t.hideturtle()


t.done()
