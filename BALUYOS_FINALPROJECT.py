import turtle as t

t.pensize(6)
	
def headshape():
	
	t.penup()
	t.goto(22,322)
	t.pendown()

	t.setheading(25)
	t.circle(-150,85)
	
	t.setheading(300)
	t.circle(-450,50)
	
	t.setheading(250)
	t.circle(600,20)
	
	t.penup()
	t.goto(-150,-330)
	t.pendown()
	
	t.setheading(80)
	t.circle(-850,15)
	
	t.penup()
	t.goto(-140,-108)
	t.pendown()
	
	t.setheading(340)
	t.circle(200,120)
	
	t.penup()
	t.goto(-140,-108)
	t.pendown()
	
	t.setheading(170)
	t.circle(-30,90)
	
	t.penup()
	t.goto(-180,-58)
	t.pendown()
	
	t.setheading(330)
	t.circle(200,30)
	
	t.penup()
	t.goto(-180,-58)	
	t.pendown()
	
	t.setheading(160)
	t.circle(-50,145)
	
	t.penup()
	t.goto(-176,50)
	t.pendown()
	t.setheading(270)
	t.forward(45)
	
	t.penup()
	t.goto(-180,5)
	t.pendown()
	
	t.setheading(320)
	t.circle(200,50)
	
	t.setheading(355)
	t.circle(50,70)
	
	t.setheading(65)
	t.circle(500,15)
	
	t.penup()
	t.goto(80,154)
	t.pendown()
	
	t.setheading(155)
	t.forward(20)
	
	#mouth
	t.setheading(335)
	t.circle(-30,200)
	
	t.setheading(290)
	t.forward(40)
	
	t.setheading(280)
	t.circle(-60,100)
	
	t.setheading(180)
	t.circle(-300,30)

	t.setheading(160)
	t.circle(-60,110)
	
	t.penup()
	t.goto(-197,65)
	t.pendown()
	
	t.setheading(260)
	t.circle(-30,130)
	
	t.setheading(160)
	t.circle(-15,80)
	
	t.setheading(70)
	t.circle(70,60)
	
	t.setheading(130)
	t.circle(-50,130)
	t.goto(-80,245)
	
	t.setheading(40)
	t.forward(100)
	t.goto(22,322)

def eyes():
	
	t.penup()
	t.goto(65,210)
	t.pendown()
	t.setheading(28)
	
	
	for _ in range(2):
		t.circle(50,110)
		t.circle(20,70)
		
	t.penup()
	t.goto(-25,230)
	t.pendown()
	t.setheading(2)
	
	
	for _ in range(2):
		t.circle(50,110)
		t.circle(10,70)
	
	t.fillcolor("black")	
	t.penup()
	t.goto(60,220)
	t.pendown()
	t.begin_fill()
	t.circle(13)
	t.end_fill()
	
	t.penup()
	t.goto(-5,240)
	t.pendown()
	t.begin_fill()
	t.circle(13)
	t.end_fill()
	
def nose():
	
	t.color("black","white")
	t.penup()
	t.goto(0,230)
	t.pendown()
	
	t.begin_fill()
	t.setheading(200)
	t.circle(-60,65)
	
	t.setheading(180)
	t.forward(90)
	
	t.color("white")
	t.setheading(270)
	t.forward(50)
	t.goto(0,230)
	t.end_fill()

	t.color("black","black")
	t.penup()
	t.goto(-142,245)
	t.pendown()
	
	t.begin_fill()
	t.setheading(180)
	t.forward(30)
	
	t.setheading(180)
	t.circle(50,120)
	t.setheading(300)
	t.forward(30)
	
	t.setheading(300)
	t.circle(30,80)
	
	t.setheading(20)
	t.forward(60)
	
	t.setheading(20)
	t.circle(30,110)
	
	t.setheading(140)
	t.forward(73)
	t.end_fill()
	
def brows():
	t.fillcolor("black")
	t.penup()
	t.goto(-25,330)
	t.pendown()
	
	t.begin_fill()
	t.setheading(40)
	t.circle(-60,60)
	t.setheading(320)
	t.circle(-15,200)
	t.setheading(200)
	t.forward(20)
	t.setheading(200)
	t.circle(-15,100)
	t.end_fill()
	
	t.penup()
	t.goto(95,350)
	t.pendown()
	
	t.begin_fill()
	t.setheading(320)
	t.circle(-80,50)
	t.setheading(280)
	t.circle(-15,180)
	t.setheading(100)
	t.forward(30)
	t.setheading(100)
	t.circle(15,100)
	t.setheading(145)
	t.circle(-15,170)
	t.goto(95,350)
	t.end_fill()
	
def ear1():
	
	t.penup()
	t.goto(-10,330)
	t.pendown()
	
	t.setheading(110)
	t.circle(-150,50)
	t.setheading(60)
	t.circle(10,120)
	
	t.penup()
	t.goto(-30,325)
	t.pendown()
	
	t.setheading(200)
	t.circle(-25,140)
	t.setheading(60)
	t.forward(40)
	
	t.setheading(180)
	t.circle(-18,120)
	t.setheading(60)
	t.forward(60)
	t.setheading(60)
	t.circle(-22,190)
	t.setheading(240)
	t.circle(25,100)
	t.setheading(330)
	t.circle(-65,83)

def ear2():
	
	t.penup()
	t.goto(165,280)
	t.pendown()
	
	t.begin_fill()
	t.setheading(65)
	t.forward(100)
	t.setheading(65)
	t.circle(-25,110)
	t.setheading(300)
	t.circle(20,130)
	t.setheading(50)
	t.forward(10)
	t.setheading(50)
	t.circle(-20,120)
	t.setheading(280)
	t.circle(-75,50)
	t.setheading(210)
	t.circle(-45,70)
	t.setheading(160)
	t.forward(20)
	t.setheading(280)
	t.circle(-105,40)
	t.color("white")
	t.goto(275,315)
	t.setheading(320)
	t.color("black")
	t.circle(-55,40)
	t.setheading(280)
	t.circle(-25,60)
	t.setheading(220)
	t.forward(75)
	t.color("white")
	t.goto(165,280)
	t.end_fill()
	
def collar():
	
	t.color("black")
	t.penup()
	t.goto(-150,-300)
	t.pendown()
	
	t.setheading(190)
	t.circle(15,160)
	t.setheading(340)
	t.circle(505,42)
	t.setheading(10)
	t.circle(15,160)
	
	t.penup()
	t.goto(-140,-280)
	t.pendown()
	
	t.setheading(180)
	t.circle(45,70)
	t.setheading(266)
	t.forward(80)
	t.setheading(335)
	t.circle(505,50)
	t.setheading(90)
	t.forward(75)
	t.setheading(90)
	t.circle(45,65)
	
	
headshape()
eyes()
nose()
brows()
ear1()
ear2()
collar()

t.hideturtle()
t.done()