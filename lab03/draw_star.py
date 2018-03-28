from turtle import *
def starz(x,y,le):
    penup()
    goto(x,y)
    pendown()

    left(36)
    forward(le)
    for o in range(4):
        left(144)
        forward(le)
    # mainloop()
