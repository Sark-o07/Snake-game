from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# setting the screen attributes
screen.setup(width=600, height=600)
screen.title("Agwo turu mbe")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun= snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.5)

    snake.move()

    # detecting collision btw snake head and food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.update_score()

    # detecting collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()











screen.exitonclick()

