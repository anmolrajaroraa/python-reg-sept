import turtle
import random

s = turtle.Screen()
s.bgcolor('black')
t = turtle.Pen()
t.shape('turtle')
t.turtlesize(2,2)
t.speed(0)
t.width(3)
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise']
#shapes= ['square', 'triangle', 'hexagon', 'dot', 'circle']
shapes = list(range(5))

for i in range(100):
    t.color(random.choice(colors))
    shape = random.choice(shapes)
    if shape == 0:
        for i in range(4):
            t.forward(100)
            t.left(90)
    elif shape == 1:
        for i in range(3):
            t.forward(100)
            t.left(120)
    elif shape == 2:
        for i in range(6):
            t.forward(100)
            t.left(60)
    elif shape == 3:
        t.dot(50)
    elif shape == 4:
        t.circle(50)
    else:
        print('shape not found')
    x = random.choice(range(-300, 300))
    y = random.choice(range(-300, 300))
    t.penup()
    t.setposition(x,y)
    t.pendown()
