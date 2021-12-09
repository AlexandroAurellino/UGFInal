import turtle

jhoncena = turtle.Turtle()

#background
jhoncena = turtle.color("blue","cyan")
jhoncena = turtle.begin_fill()
jhoncena = turtle.penup()
jhoncena = turtle.goto(-350,-50)
jhoncena = turtle.pendown()
jhoncena = turtle.forward(570)
jhoncena = turtle.left(90)
jhoncena = turtle.forward(280)
jhoncena = turtle.left(90)
jhoncena = turtle.forward(570)
jhoncena = turtle.left(90)
jhoncena = turtle.forward(280)
jhoncena = turtle.left(90)
jhoncena = turtle.end_fill()

jhoncena = turtle.color("blue")


#start point
jhoncena = turtle.penup()
jhoncena = turtle.goto(-300,0)
jhoncena = turtle.pendown()

#huruf A
jhoncena = turtle.left(70)
jhoncena = turtle.forward(190)
jhoncena = turtle.right(140)
jhoncena = turtle.forward(190)
jhoncena = turtle.penup()
jhoncena = turtle.right(150)
jhoncena = turtle.forward(130)
jhoncena = turtle.pendown()
jhoncena = turtle.right(140)
jhoncena = turtle.forward(70)

#huruf L
jhoncena = turtle.penup()
jhoncena = turtle.goto((150-300),180)
jhoncena = turtle.pendown()
jhoncena = turtle.right(90)
jhoncena = turtle.forward(180)
jhoncena = turtle.left(90)
jhoncena = turtle.forward(100)

#huruf E
jhoncena = turtle.penup()
jhoncena = turtle.goto((260-300),180)
jhoncena = turtle.pendown()
jhoncena = turtle.forward(100)
jhoncena = turtle.penup()
jhoncena = turtle.goto((260-300),180)
jhoncena = turtle.pendown()
jhoncena = turtle.right(90)
jhoncena = turtle.forward(180)
jhoncena = turtle.penup
jhoncena = turtle.goto((260-300),90)
jhoncena = turtle.pendown()
jhoncena = turtle.left(90)
jhoncena = turtle.forward(100)
jhoncena = turtle.penup()
jhoncena = turtle.goto((260-300),0)
jhoncena = turtle.pendown()
jhoncena = turtle.forward(100)

#huruf X
jhoncena = turtle.penup()
jhoncena = turtle.goto((370-300),0)
jhoncena = turtle.pendown()
jhoncena = turtle.left(65)
jhoncena = turtle.forward(200)
jhoncena = turtle.penup()
jhoncena = turtle.goto((370-300),180)
jhoncena = turtle.pendown()
jhoncena = turtle.right(125)
jhoncena = turtle.forward(200)

#underline
jhoncena = turtle.penup()
jhoncena = turtle.goto(-300,-15)
jhoncena = turtle.left(60)
jhoncena = turtle.pendown()
jhoncena = turtle.forward(470)

#topline
jhoncena = turtle.penup()
jhoncena = turtle.goto(-300,197)
jhoncena = turtle.pendown()
jhoncena = turtle.forward(470)


turtle.done()