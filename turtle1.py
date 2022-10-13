import math
import turtle

#Named constants
window_width = 400
window_height = 400
animation_speed = 0
num_sides = 8
length = 100
angle = 45
text_x = -5
text_y = -10

#Size the window
turtle.setup(window_width, window_height)

#diameter
s = length
x = s / math.sqrt(2)
diameter = s + (2*x)

#draw
turtle.fillcolor("red")
turtle.begin_fill()
for x in range(8):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

turtle.penup()
writing = turtle.Turtle()
writing.penup()
writing.goto(0, -150)
writing.color("white")
writing.write("STOP", font = ("Impact", "50"))
writing.hideturtle()
