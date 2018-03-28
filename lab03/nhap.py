
from turtle import*
def drSquare(le, color):
    shape("turtle")

    pencolor(color)
    for i in range(4):
        forward(le)
        left(90)
    # mainloop()

# drSquare(100,"red")

for i in range(30):
    drSquare(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
