import turtle
wn = turtle.Screen()
wn.title("Exercicio 3.11")
wn.bgcolor("white")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("black")


# desenha a estrela
alex.speed(1)
alex.left(36)
for i in range(5):
	alex.forward(200)
	alex.left(144)

wn.mainloop()
