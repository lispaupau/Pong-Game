from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.title('Pong')
screen.setup(width=800, height=600)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        score.l_point()

    # Detect L paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
