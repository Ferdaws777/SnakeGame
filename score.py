from turtle import Turtle
FONT = ("Arial", 16,"normal")
ALIGNMENT = "center"

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,275)
        self.write(f"Score: {self.score}", font=FONT, align= ALIGNMENT)
        self.hideturtle()
    
    
    def add_score(self):
        self.clear()
        self.score += 5
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
    
    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.write(f"Game Over\n Your final Score is: {self.score}",font=FONT,align=ALIGNMENT)
        