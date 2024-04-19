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




