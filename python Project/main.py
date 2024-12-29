import turtle as t
s = t.Turtle()
s = t.Turtle()
s.speed(0) 
s.color("black","black")
s.penup()
s.backward(600)
s.pendown()
for k in range(8):
    for j in range(1,9):
        if(j%2==0):
            s.begin_fill()

            for i in range(4):
                s.forward(200)
                s.right(90)
            s.end_fill()
        else:
            
            for i in range(4):
                s.forward(200)
                s.right(90)

        s.forward(200)
    s.right(90)
    s.forward(200)
    s.right(90)
    s.penup()
    s.forward(1600)
    s.right(180)
    s.pendown()