from turtle import *

leo=Turtle()

leo.color('purple')
leo.pensize(6)
leo.speed(8)
leo.shape('turtle')

def drawtriangle():
	for x in range (3):
		leo.forward(100)
		leo.left(120)

for x in range (18):
	drawtriangle()
	leo.left(30)

mainloop()

