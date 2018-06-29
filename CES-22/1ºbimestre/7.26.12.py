import turtle


wn = turtle.Screen()
wn.title("Exercicio 7.26.12")
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("red")
alex.speed(speed=1)
lista = [(180,50), (135,70.5), (135, 50), (135, 70.5), (75, 50), (120, 50), (120, 50), (-90, 50)]

for i in lista:
	alex.right(i[0])
	alex.forward(i[1])

wn.mainloop()
