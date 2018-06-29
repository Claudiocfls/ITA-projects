import turtle

def draw_star(alex):
	alex.left(36)
	for i in range(5):
		alex.forward(100)
		alex.left(144)
	alex.right(36)

wn = turtle.Screen()
wn.title("Exercicio 4.9.10")
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("red")

angle = 144
alex.penup()
alex.forward(200)
alex.pendown()
for i in range(5):
	draw_star(alex)
	alex.penup()
	alex.left(angle)
	alex.forward(350)
	alex.right(angle)
	angle += 72
	alex.pendown()

wn.mainloop()
