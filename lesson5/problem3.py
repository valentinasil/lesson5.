from turtle import *

leo=Turtle()

leo.color('purple')
leo.pensize(6)
leo.speed(8)
leo.shape('turtle')


for x in range (6):
	leo.forward(80)
	leo.left(60)

mainloop()
