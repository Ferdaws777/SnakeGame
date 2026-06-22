
from  turtle import Turtle


FONT = ("Elephant", 16,"normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("Black")
        self.goto(0,270)
        self.write(arg=f"Score:{self.score}", move=False, align=ALIGNMENT, font= FONT)
        self.hideturtle()


    def easy_score(self):
        self.clear()
        self.score +=2
        self.write(arg=f"Score:{self.score}", move=False, align="center", font= FONT)

    def max_sccore(self):
        self.clear()
        self.score += 24
        self.write(arg=f"Score:{self.score}", move=False, align="center", font=FONT)


    def medium_score(self):
        self.clear()
        self.score +=4
        self.write(arg=f"Score:{self.score}", move=False, align="center", font=FONT)

    def hard_score(self):
        self.clear()
        self.score +=8
        self.write(arg=f"Score:{self.score}", move=False, align="center", font=FONT)


    def game_over(self):
        self.clear()
        self.penup()
        self.color("Blue")
        self.goto(0, 0)
        self.write(f"Game Over! and you have got {self.score} Score", font= FONT, align=ALIGNMENT)


    def reset(self):
        self.score = 0
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score:{self.score}", move=False, align=ALIGNMENT, font= FONT)
