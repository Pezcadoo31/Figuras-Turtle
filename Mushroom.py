import turtle
t = turtle.Turtle()
t.pensize(5)

turtle.bgcolor("black")

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t.pencolor("#5D4037")
t.fillcolor("#FF0000")

go(-200, 0)

t.begin_fill()
t.goto(200,0)
t.circle(70,90)
t.seth(90)
t.circle(266,180)
t.seth(270)
t.circle(70,90)
t.end_fill()

t.pencolor("#5D4037")
t.fillcolor("#FAD7A0")

go(-120, -5)

t.begin_fill()
t.seth(270)
t.goto(-120,-180)
t.circle(45,90)
t.goto(75,-225)
t.circle(45,90)
t.goto(120,-5)
t.end_fill()

t.pencolor("#5D4037")
t.fillcolor("#FFFFFF")

go(100, 220)

t.begin_fill()
t.circle(60)
go(-120, 70)
t.circle(30)
t.end_fill()

go(200, 0)

t.begin_fill()
t.circle(50, 180)
t.end_fill()

t.pencolor("#5D4037")
t.fillcolor("#000000")

go(-20, -70)

t.begin_fill()
t.seth(90)
t.circle(25, 180)
t.goto(-70, -90)
t.circle(25, 180)
t.goto(-20, -70)
go(70,-70)
t.circle(25, 180)
t.goto(20, -90)
t.circle(25, 180)
t.goto(70, -70)
t.end_fill()

t.pencolor("#FFFFFF")
t.fillcolor("#FFFFFF")

go(-45, -70)

t.begin_fill()
t.seth(90)
t.circle(10)
go(45,-70)
t.circle(10)
t.end_fill()

t.pencolor("#000000")
t.fillcolor("#FF0080")

go(45, -150)

t.begin_fill()
t.goto(-45, -150)
t.seth(270)
t.circle(45, 180)
t.end_fill()

t.hideturtle()
turtle.exitonclick()
