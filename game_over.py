from score import Score

FONT = ("Arial", 20 ,"normal")
ALIGNMENT = "center"


class GameOver(Score):
    def __init__(self):
        super().__init__()
        
    def game_over(self):
        
        self.penup()
        self.goto(0,0)
        self.write(f"Game Over\n Your final Score is: {self.score}",font=FONT,align=ALIGNMENT)
        