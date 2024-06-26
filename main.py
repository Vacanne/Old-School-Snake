from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Old School Snake")
screen.tracer(0)  # Turn off screen updates

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control the snake with keyboard inputs
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_on = True

while game_on:
    screen.update()  # Refresh the screen
    time.sleep(0.1)  # Control the speed of the game
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.respawn()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
