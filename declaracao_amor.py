import turtle
d = turtle.Turtle()
def figura():
   for i  in range(200):
      d.right(1)
      d.forward(1)
def cora():
   d.color('pink')  
   d.begin_fill()  
   d.left(140)
   d.forward(113)
   figura()
   d.left(120)  
   figura()
   d.forward(112)
   d.end_fill()
   
def texto():
      d.up()
      d.setpos(-68,90)
      d.down()
      d.color('black')
      d.write('    Te Amo', font=("verdana", 18, "bold"))
     
tela = turtle.Screen()
tela.textinput("","Diga sim pra mim!!")
p = turtle.title("My declaration in Python")
tela.turtles = turtle.bgcolor('red')
cora()
texto()
d.ht()

