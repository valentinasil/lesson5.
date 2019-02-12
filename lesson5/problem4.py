from turtle import *

leo=Turtle()

leo.color('purple')
leo.pensize(6)
leo.speed(8)
leo.shape('turtle')

def drawhexagon(side):
	for x in range (6):
		leo.forward(side)
		leo.left(60)


drawhexagon(10)
drawhexagon(20)
drawhexagon(30)
drawhexagon(40)
drawhexagon(50)
drawhexagon(60)
drawhexagon(70)
drawhexagon(80)
drawhexagon(90)


mainloop()
