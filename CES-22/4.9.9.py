import turtle

def draw_star(alex):
	alex.left(36)
	for i in range(5):
		alex.forward(100)
		alex.left(144)

wn = turtle.Screen()
wn.title("Exercicio 4.9.9")
wn.bgcolor("white")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("black")

draw_star(alex)


wn.mainloop()
