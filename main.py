
from turtle import Screen
from snake import Snake
import time
screen = Screen()
screen.title("MY SnakeGame")
screen.setup(width=600,height=600)
screen.bgcolor("Black")

screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()







screen.exitonclick()


# segment1= Turtle("square")
# segment1.color("white")
# segment2= Turtle("square")
# segment2.color("white")
# segment2.goto(x=-20,y=0)
# segment3= Turtle("square")
# segment3.color("white")
# segment3.goto(x=-40,y=0)