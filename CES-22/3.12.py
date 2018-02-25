import turtle
wn = turtle.Screen()
wn.title("Exercicio 3.12")
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")


# desenha o relógio
alex.penup()

for i in range(12):
	alex.forward(160)
	alex.pendown()
	alex.forward(10)
	alex.penup()
	alex.forward(30)
	alex.stamp()
	alex.backward(200)
	alex.left(30)

alex.stamp()

wn.mainloop()
