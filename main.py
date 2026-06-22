
from turtle import Screen
from snake import Snake
from  food import Food
from score import Score
import time

screen = Screen()
screen.title("MY SnakeGame")
screen.setup(width=600,height=600)
screen.onscreenclick(1,1)
Screen_color_choice = screen.textinput(title="Select your screen mode",prompt="please type Dard or Light ")

Level_choice = screen.textinput(title="Select your Game Level",prompt="please type (easy,medium or hard")

def turn_on():
    global game_is_on
    game_is_on = True

screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

if Screen_color_choice.lower() == "dark":
    screen.bgcolor("black")
    score.color("white")
elif Screen_color_choice.lower() == "light":
    screen.bgcolor("white")
else:
    print("Wrong Input")

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


def restart_game():
    turn_on()
    screen.update()
    screen.listen()
    snake.reset()
    score.reset()
                 

game_is_on = True
while game_is_on:
    screen.update()
    if Level_choice.lower() == "easy":
        time.sleep(0.25)
        snake.move()

    elif Level_choice.lower() == "medium":
        time.sleep(0.2)
        snake.move()

    elif Level_choice.lower() == "hard":
        time.sleep(0.1)
        snake.move()
    else:
        game_is_on = False
        print("wrong input for level")


    if snake.head.distance(food) < 15:
        if score.score != 0 and score.score % 5 == 0:
            food.refresh()
            snake.extend()
            score.max_sccore()
        else:
            if Level_choice.lower() == "easy":
                food.refresh()
                snake.extend()
                score.easy_score()

            elif Level_choice.lower() == "medium":
                food.refresh()
                snake.extend()
                score.medium_score()

            elif Level_choice.lower() == "hard":
                food.refresh()
                snake.extend()
                score.hard_score()



    if snake.head.xcor() >285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.game_over()
        retry = screen.textinput(title="Game Over", prompt="Do you want to play again? (yes or no)")
        if retry and retry.lower() == "yes":
            restart_game()
             
        elif retry and retry.lower() == "no":
            game_is_on = False
        else:
            print("wrong input")
            

    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            retry = screen.textinput(title="Game Over", prompt="Do you want to play again? (yes or no)")
            
            if retry and retry.lower() == "yes":
                restart_game()
            else:
                game_is_on = False
                score.game_over()

    



screen.exitonclick()


