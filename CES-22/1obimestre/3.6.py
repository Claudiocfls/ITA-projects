import turtle
wn = turtle.Screen()
wn.title("Exercicio 3.6")
wn.bgcolor("white")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")

# move alex para o lado esquerdo da tela
alex.penup()
alex.backward(300)
alex.pendown()

# desenha o triangulo equilatero    
alex.begin_fill()        
alex.color("red")
for i in range(3):        
   alex.forward(100)       
   alex.left(120)    
alex.end_fill()

# desenha um quadrado
alex.penup()
alex.forward(110)
alex.pendown()
alex.begin_fill()    
alex.color("blue")
for i in range(4):        
   alex.forward(100)       
   alex.left(90)   
alex.end_fill()

# desenha um hexágono
alex.penup()
alex.forward(150)
alex.pendown()
alex.begin_fill()    
alex.color("yellow")
for i in range(6):        
   alex.forward(65)       
   alex.left(60)   
alex.end_fill()

# desenh um octógno
alex.penup()
alex.forward(150)
alex.pendown()
alex.begin_fill()    
alex.color("green")
for i in range(8):        
   alex.forward(45)       
   alex.left(45)   
alex.end_fill()

wn.mainloop()
