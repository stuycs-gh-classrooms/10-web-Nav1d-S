import turtle
window = turtle.Screen()
window.setup(900, 600)

def draw_koch(t, depth, length):
    t.pd()
    if depth == 1:
        t.forward(length)
    else:
        draw_koch(t, depth - 1, length / 3)
        t.lt(60)
        draw_koch(t, depth - 1, length / 3)
        t.rt(120)
        draw_koch(t, depth - 1, length / 3)
        t.lt(60)
        draw_koch(t, depth - 1, length / 3)
        t.bk(length)
        draw_koch(t, depth - 1, length / 3)
        t.lt(60)
        draw_koch(t, depth - 1, length / 3)
        t.rt(120)
        draw_koch(t, depth - 1, length / 3)
        t.lt(60)
        draw_koch(t, depth - 1, length / 3)

t = turtle.Turtle()
draw_koch(t, 4, 300)
t.pu()
t.goto(-295, 290)
t.pd()

window.exitonclick()






