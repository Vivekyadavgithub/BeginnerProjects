import turtle
import time

root = turtle.Screen()
root.title = ("created by vivek")
root.setup(width = 800, height= 600)
root.bgpic("moon.png")
#root.tracer(0,100)

slab = turtle.Turtle()
slab.speed(0)
slab.shape("square")
slab.color("blue","white")
slab.shapesize(stretch_wid=3,stretch_len=8)
slab.penup()
slab.goto(0, -290)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue","white")
ball.penup()
ball.goto(0,0)
ball.dx = 6
ball.dy = 6

px, py = -350, 200
totalpoint = 110
piece = 1
for i in range(totalpoint):
  if piece == 1:
    point = turtle.Turtle()
    point.speed(0)
    point.shape("square")
    point.color("red","yellow")
    point.penup()
    point.goto(px, py)
    piece -= 1

  else:
      point = turtle.Turtle()
      point.speed(0)
      point.shape("square")
      point.color("yellow","red")
      point.penup()
      point.goto(px, py)
      piece += 1

  if i == 28 or i ==55 or i == 82:
      py -= 25
      px = -350

  px += 25

# for movement of the slab
def left():
    x = slab.xcor()
    x -= 5
    slab.setx(x)

def right():
    x = slab.xcor()
    x += 5
    slab.setx(x)

root.listen()
root.onkeypress(left,"a")
root.onkeypress(right,"d")


gameover = False

while not gameover:
   #root.update()
   ball.setx(ball.xcor() + ball.dx)
   ball.sety(ball.ycor() + ball.dy)

   if ball.xcor() > 400 or ball.xcor() < -400:
       ball.dx *= -1

   if ball.ycor() > 300:
        ball.dy *= -1

   if ball.ycor() < -300:
     ball.goto(0,0)
     time.sleep(1)

   if (ball.ycor() < -260 and ball.ycor() > -290) and (ball.xcor() < slab.xcor() + 80 and ball.xcor() > slab.xcor() - 80):
       ball.sety(-260)
       ball.dy *= -1

   if ball.xcor() == point.xcor() and ball.ycor() == point.ycor():
       ball.dy *= -1
       point.penup()
       point.goto(1000,1000)

turtle.done()