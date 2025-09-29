from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
from high_score_tracker import  HighScoreTracker
from music_controller import init_audio, play_game_music, stop_music, play_sfx

screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

init_audio()
play_game_music(volume=0.4)   # start music BEFORE the game loop

snake = Snake()
food = Food()
scoreboard = ScoreBoard(tracker=HighScoreTracker())

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 18:
        play_sfx("eat")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        play_sfx("pain")
        stop_music()
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 18:
            game_is_on = False
            play_sfx("pain")
            stop_music()
            scoreboard.game_over()
    #if head collects with any segment in tail then game over


screen.exitonclick()

