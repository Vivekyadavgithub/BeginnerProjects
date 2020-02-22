import turtle
import winsound
wn = turtle.Screen()
wn.title=("created by vivek")
wn.bgcolor("blue")
wn.setup(width=800,height=600)
#wn.tracer(6,50)

paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)


paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=8
ball.dy=8

# for score
score1 = 0
score2 =0
#default score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player a: {} player b: {}".format(score1 , score2),  align ="center", font=("courier",24,"normal"))

def paddle1up():
      y=paddle1.ycor()
      y +=20
      paddle1.sety(y)


def paddle1down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddle2down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

wn.listen()
wn.onkeypress(paddle1up,"w")
wn.onkeypress(paddle1down,"s")
wn.onkeypress(paddle2up,"Up")
wn.onkeypress(paddle2down,"Down")
gameover=False
while  not False:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 +=1
        pen.clear()
        pen.write("player a: {} player b: {}".format(score1, score2), align="center", font=("courier", 24, "normal"))
        soundfile = "gunshot.wav"
        winsound.PlaySound(soundfile, winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2  += 1
        pen.clear()
        pen.write("player a: {} player b: {}".format(score1, score2), align="center", font=("courier", 24, "normal"))
        soundfile="gunshot.wav"
        winsound.PlaySound(soundfile,winsound.SND_ASYNC)



    #collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and(ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1