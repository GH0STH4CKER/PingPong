import turtle,keyboard,random

# Create Screen
sc = turtle.Screen()
sc.title("Ping Pong Game")
sc.bgcolor('black') #(0.75,0.84,0.92)
sc.setup(width=1000, height=600)  # Game window size

# Draw Border 
t = turtle.Turtle()
t.speed(0)
t.color((0,0.8,0.8))
t.pensize(5)
t.hideturtle()
t.penup()
t.goto(-490,290) 
l = 975
w = 575
t.pendown()
t.forward(l)
t.right(90) 
t.forward(w)
t.right(90) 
t.forward(l)
t.right(90) 
t.forward(w)
t.right(90) 

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color((0,0.9,0))
left_pad.shapesize(stretch_wid=6, stretch_len=1)
left_pad.penup()
left_pad.goto(-400, 0)


# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color((0,0.9,0))
right_pad.shapesize(stretch_wid=6, stretch_len=1)
right_pad.penup()
right_pad.goto(400, 0)


# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color('cyan','blue')
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 8
hit_ball.dy = -8


# Initial Score
Computer = 0
Player = 0


# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color((0,0.5,0.9))
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 240)
sketch.write("Computer : 0                Player : 0",
			align="center", font=("Comic Sans MS", 24, "normal"))

# Moving paddles vertically

def paddleAup():     
	y = left_pad.ycor()
	if left_pad.ycor() <= 220 :  # Stop paddles going out of range
		y += 20
		left_pad.sety(y)		 # Moving paddle 


def paddleAdown():
	y = left_pad.ycor()
	if left_pad.ycor() >= -220 :
		y -= 20
		left_pad.sety(y)


def paddleBup():
	y = right_pad.ycor()
	if right_pad.ycor() <= 220 :
		y += 20
		right_pad.sety(y)


def paddleBdown():
	y = right_pad.ycor()
	if right_pad.ycor() >= -220 :
		y -= 20
		right_pad.sety(y)


# Keyboard bindings
sc.listen()
sc.onkeypress(paddleAup, "w")           # Player 1 COntrols 
sc.onkeypress(paddleAdown, "s")         # W / S KEY

sc.onkeypress(paddleBup, "Up")          # Player 2 Controls
sc.onkeypress(paddleBdown, "Down")      # UP / DOWN ARROW

rn = 0

while True:
	sc.update()
		
	# Computer move paddle 	
	rn2 = random.randint(2,6) 
	if hit_ball.xcor() < 100 :
		
		rn = random.randint(10,50)
		if rn%rn2 == 0 :
			rn = random.randint(10,100)
			if rn%2 == 0 :
				left_pad.sety(hit_ball.ycor()-50+rn)


	hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
	hit_ball.sety(hit_ball.ycor()+hit_ball.dy)


	# Checking borders
	if hit_ball.ycor() > 280:
		hit_ball.sety(280)
		hit_ball.dy *= -1

	if hit_ball.ycor() < -280:
		hit_ball.sety(-280)
		hit_ball.dy *= -1

	if hit_ball.xcor() > 500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		Computer += 1
		sketch.clear()
		sketch.write("Computer : {}                Player: {}".format(
					Computer, Player), align="center",
					font=("Comic Sans MS", 24, "normal"))

	if hit_ball.xcor() < -500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		Player += 1
		sketch.clear()
		sketch.write("Computer : {}                Player: {}".format(
								Computer, Player), align="center",
								font=("Comic Sans MS", 24, "normal"))

	# Ball hit paddle
	if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+80 and hit_ball.ycor() > right_pad.ycor()-80):
		hit_ball.setx(360)
		hit_ball.dx*=-1

	if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor() < left_pad.ycor()+80 and hit_ball.ycor() > left_pad.ycor()-80):
		hit_ball.setx(-360)
		hit_ball.dx*=-1
