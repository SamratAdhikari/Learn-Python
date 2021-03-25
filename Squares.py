print("Squares")
import turtle

samrat = turtle.Turtle()


samrat.speed(2)

samrat.color("purple", "cyan")

samrat.begin_fill()


for i in range(4):


    samrat.forward(100)
    samrat.left(90)
samrat.right(90)

samrat.penup()
samrat.forward(100)
samrat.pendown()

for i in range(4):


    samrat.forward(100)
    samrat.left(90)


samrat.end_fill()
turtle.done()

