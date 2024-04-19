import turtle
import random
window = turtle.Screen()
window.setup(900, 600)

def draw_koch(t, depth, length):
    t.pd()
    chance = random.randrange(2)
    if depth == 1:
        t.forward(length)
        if chance != 1:
            t.color('red')
        else:
            t.color('blue')
    else:
        if chance != 2:
            angle = random.randrange(60, 120)
        else:
            angle = 60
        draw_koch(t, depth - 1, length / 3)
        t.lt(angle)
        draw_koch(t, depth - 1, length / 3)
        t.rt(120)
        draw_koch(t, depth - 1, length / 3)
        t.lt(angle)
        draw_koch(t, depth - 1, length / 3)
        t.bk(length)
        draw_koch(t, depth - 1, length / 3)
        t.lt(-angle)
        draw_koch(t, depth - 1, length / 3)
        t.rt(-120)
        draw_koch(t, depth - 1, length / 3)
        t.lt(-angle)
        draw_koch(t, depth - 1, length / 3)

t = turtle.Turtle()
draw_koch(t, 3, 300)
t.pu()
t.goto(-295, 290)
t.pd()

window.exitonclick()


import turtle
import random
window = turtle.Screen()
window.setup(900, 600)

def triangle(t, size):
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(180)

def sierpinski(t, depth, size, scale_factor=1):
    color = random.randrange(4)
    colors = ['red', 'orange', 'green', 'blue']
    t.color(colors[color])
    random_size = random.randrange(50, 300)
    size = random_size
    
    if depth == 1:
        triangle(t, size)
    else:
    
        sierpinski(t, depth-1, size/2)
        t.fd(size/2)
        sierpinski(t, depth-1, size/2)
        t.bk(size/2)
        t.lt(60)
        t.fd(size/2)
        t.rt(60)
        sierpinski(t, depth-1, size/2)
        t.rt(120)
        t.fd(size/2)
        t.lt(120)

michelangelo = turtle.Turtle()
michelangelo.pu()
michelangelo.speed(0)
michelangelo.goto(-295, 0)
michelangelo.pd()
sierpinski(michelangelo, 5, 'size')

window.exitonclick()


import turtle
import random
window = turtle.Screen()
window.setup(600, 600)

def tree(t, depth, size, angle):
    variable_size = random.randrange(50, 100)
    size = variable_size
    variable_angle = random.randrange(20, 50)
    angle = variable_angle
    colors= ['red', 'orange', 'green']
    color = random.randrange(3)
    line_color = colors[color]
    t.color(line_color)
    if depth == 0:
        t.fd(size)
        t.bk(size)
    else:
        t.fd(size)
        t.rt(angle)
        tree(t, depth-1, size, angle)
        t.lt(2 * angle)
        tree(t, depth-1, size, angle)
        t.rt(angle)
        t.bk(size)


leonardo = turtle.Turtle()
leonardo.lt(90)
leonardo.pd()
tree(leonardo, 6, 'size', 'angle')

window.exitonclick()





