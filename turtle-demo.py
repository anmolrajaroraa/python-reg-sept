#anmolarora1711@gmail.com
import turtle
import random

t = turtle.Pen()
t.shape('turtle')
t.color('blue')
#speed can be given from 0.5 (slow) till 10 (fast), if any other value is given,
#it takes it as 0 (fastest)
t.speed(0)
colors = ['red', 'green', 'blue']

for i in range(200):
    x = random.choice(range(-300,300))
    y = random.choice(range(-300,300))
    randomColor = random.choice(colors)
    t.color(randomColor)
    t.penup()
    #t.setposition(x,y)
    t.pendown()
    #for i in range(4):
        #t.forward(100)
        #t.right(90)
    #t.circle(2 * i)
    #t.left(10)
    #t.dot(25)
    size = 3 * i
    for j in range(3):
        t.forward(3 * i)
        t.left(120)
    #t.left(10)
        
    
